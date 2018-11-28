import requests
from bs4 import BeautifulSoup, SoupStrainer
import csv
import re

#profiles to get data from
names = ["momomomo"]
#list of games already read
game_ids = set()
#list of summoners already checked
used_names = set()
#counter to stop
n_max = 5000
n_current = 0

#open csv file
with open('game_data_2.csv', 'a') as file:
    writer = csv.writer(file, delimiter=',', lineterminator='\n')
    while (n_current < n_max) or names:
        print(n_current)
        n_current += 1
        #get summoner name and add to list of used
        current_name = names.pop()
        used_names.add(current_name)
        #open summoner page
        url = "http://na.op.gg/summoner/userName=" + current_name
        r = requests.get(url)
        #reduce to necessary part
        strainer = SoupStrainer('div', {'class':'GameItemWrap'})
        #Pass html to BeautifulSoup
        soup = BeautifulSoup(r.text, 'lxml', parse_only=strainer)
        #Get source code for all games
        games = soup.find_all(name='div', class_ = 'GameItemWrap')
        for game in games:
            #Check if GameType is ARAM
            game_type = game.find(class_ = 'GameType').string
            game_type = re.sub('\n|\t', '', game_type)
            if game_type != 'ARAM':
                continue
            #get game id and make sure it is not duplicate
            game_id = game.find('div')['data-game-id']
            if game_id in game_ids:
                continue
            else:
                game_ids.add(game_id)
            #Store info for game in order (W/L, time,  allies, enemies)
            info = []
            #Victory or Defeat
            game_result = game.find(class_ = 'GameResult').string
            game_result = re.sub('\n|\t', '', game_result)
            #Games under a certain length are classified as remake; exclude these
            if game_result == 'Remake':
                continue
            info.append(game_result)
            #Game Length in seconds
            game_length = game.find(class_ = 'GameLength').string
            game_length = re.sub('m|s', '', game_length)
            min, sec = game_length.split()
            info.append(int(min) * 60 + int(sec))
            #Get both teams
            team1, team2 = game.find_all(class_ = 'Team')
            #Find out which is friend/enemy by checking for Summoner Requester
            if team1.find(class_ = 'Summoner Requester') != None:
                ally = team1
                enemy = team2
            else:
                ally = team2
                enemy = team1
            #Ally Champion list
            for summoner in ally.find_all(class_ = 'Summoner'):
                #get champion of summoner
                info.append(summoner.find(class_ = re.compile('Image16')).string)
                #get name of summoner and add to list for scraping
                name = summoner.find(class_ = 'SummonerName').find('a').string
                name = str(name)
                if name not in used_names:
                    names.append(re.sub(' ', '', name))
            #Enemy Champion list
            for summoner in enemy.find_all(class_ = 'Summoner'):
                info.append(summoner.find(class_ = re.compile('Image16')).string)
                name = summoner.find(class_ = 'SummonerName').find('a').string
                name = str(name)
                if name not in used_names:
                    names.append(re.sub(' ', '', name))
            #for test purposes
            info.append(game_type)
            writer.writerow(info)
