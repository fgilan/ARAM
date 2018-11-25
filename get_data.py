from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import re
import time

names = ["momomomo", "Pootis144", "Fgilan", "yhn Moyase"]
driver = webdriver.Chrome()
for name in names:
    url = "http://na.op.gg/summoner/userName=" + name
    #Open webpage
    driver.get(url)
    #Set language to English
    driver.find_element_by_class_name("gnb-btn-setting").click()
    time.sleep(2)
    driver.find_element_by_xpath('//li[@data-locale="en_US"]').click()
    driver.find_element_by_class_name("setting__button").click()
    time.sleep(2)
    #Update
    driver.find_element_by_id("SummonerRefreshButton").click()
    time.sleep(5)
    #Click all load more buttons
    while True:
        try:
            x = driver.find_element_by_class_name("GameMoreButton")
            x.find_element_by_class_name("Button").click()
            time.sleep(4)
        except:
            break

    #Pass html to BeautifulSoup
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    #Get source code for all games
    games = soup.find_all(name='div', class_ = 'GameItemWrap')

    #open csv file
    with open('game_data.csv', 'a') as file:
        writer = csv.writer(file, delimiter=',', lineterminator='\n')
        for game in games:
            #Store info for game in order (W/L, allies, enemies)
            info = []
            #Check if GameType is ARAM
            game_type = game.find(class_ = 'GameType').string
            if 'ARAM' not in game_type:
                continue
            #Victory or Defeat
            game_result = game.find(class_ = 'GameResult').string
            game_result = re.sub('\n|\t', '', game_result)
            info.append(game_result)
            #Game Length in seconds
            game_length = game.find(class_ = 'GameLength').string
            game_length = re.sub('m|s', '', game_length)
            min, sec = game_length.split()
            info.append(int(min) * 60 + int(sec))
            #Player Champion
            summoner_requester = game.find(class_ = 'Summoner Requester')
            player_champion = summoner_requester.find(class_ =
                                                      re.compile('Image16')).string
            info.append(player_champion)
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
                #make sure it is not summoner requester
                if summoner['class'][1] == '':
                    info.append(summoner.find(class_ = re.compile('Image16')).string)
            #Enemy Champion list
            for summoner in enemy.find_all(class_ = 'Summoner'):
                info.append(summoner.find(class_ = re.compile('Image16')).string)
            writer.writerow(info)
#Close WebDriver
driver.close()
driver.quit()
