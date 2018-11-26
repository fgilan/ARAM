#Stores functions and other things used by other files
import numpy as np

champ_dic = {'Aatrox': 'Juggernaut', 'Ahri': 'Burst', 'Akali': 'Assassin',
 'Alistar': 'Vanguard', 'Amumu': 'Vanguard', 'Anivia': 'Battlemage',
 'Annie': 'Burst', 'Ashe': 'Marksman', 'Aurelion Sol': 'Battlemage',
 'Azir': 'Specialist', 'Bard': 'Catcher', 'Blitzcrank': 'Catcher',
 'Brand': 'Burst', 'Braum': 'Warden', 'Caitlyn': 'Marksman',
 'Camille': 'Diver', 'Cassiopeia': 'Battlemage', "Cho'Gath": 'Specialist',
 'Corki': 'Marksman', 'Darius': 'Juggernaut', 'Diana': 'Diver',
 'Dr. Mundo': 'Juggernaut', 'Draven': 'Marksman', 'Ekko': 'Assassin',
 'Elise': 'Diver', 'Evelynn': 'Assassin', 'Ezreal': 'Marksman',
 'Fiddlesticks': 'Specialist', 'Fiora': 'Skirmisher', 'Fizz': 'Assassin',
 'Galio': 'Warden', 'Gangplank': 'Specialist', 'Garen': 'Juggernaut',
 'Gnar': 'Specialist', 'Gragas': 'Vanguard', 'Graves': 'Specialist',
 'Hecarim': 'Diver', 'Heimerdinger': 'Specialist', 'Illaoi': 'Juggernaut',
 'Irelia': 'Diver', 'Ivern': 'Catcher', 'Janna': 'Enchanter', 'Jarvan IV': 'Diver',
 'Jax': 'Skirmisher', 'Jayce': 'Artillery', 'Jhin': 'Marksman', 'Jinx': 'Marksman',
 "Kai'Sa": 'Marksman', 'Kalista': 'Marksman', 'Karma': 'Enchanter',
 'Karthus': 'Battlemage', 'Kassadin': 'Assassin', 'Katarina': 'Assassin',
 'Kayle': 'Specialist', 'Kayn': 'Skirmisher', 'Kennen': 'Specialist',
 "Kha'Zix": 'Assassin', 'Kindred': 'Marksman', 'Kled': 'Diver', "Kog'Maw": 'Marksman',
 'LeBlanc': 'Burst', 'Lee Sin': 'Diver', 'Leona': 'Vanguard', 'Lissandra': 'Burst',
 'Lucian': 'Marksman', 'Lulu': 'Enchanter', 'Lux': 'Burst', 'Malphite': 'Vanguard',
 'Malzahar': 'Battlemage', 'Maokai': 'Vanguard', 'Master Yi': 'Skirmisher',
 'Miss Fortune': 'Marksman', 'Mordekaiser': 'Juggernaut', 'Morgana': 'Catcher',
 'Nami': 'Enchanter', 'Nasus': 'Juggernaut', 'Nautilus': 'Vanguard',
 'Nidalee': 'Specialist', 'Nocturne': 'Assassin', 'Nunu & Willump': 'Warden', 'Olaf': 'Diver',
 'Orianna': 'Burst', 'Ornn': 'Vanguard', 'Pantheon': 'Diver', 'Poppy': 'Warden',
 'Pyke': 'Assassin', 'Quinn': 'Specialist', 'Rakan': 'Catcher', 'Rammus': 'Vanguard',
 "Rek'Sai": 'Diver', 'Renekton': 'Diver', 'Rengar': 'Diver', 'Riven': 'Skirmisher',
 'Rumble': 'Battlemage', 'Ryze': 'Battlemage', 'Sejuani': 'Vanguard',
 'Shaco': 'Assassin', 'Shen': 'Warden', 'Shyvana': 'Juggernaut',
 'Singed': 'Specialist', 'Sion': 'Vanguard', 'Sivir': 'Marksman',
 'Skarner': 'Diver', 'Sona': 'Enchanter', 'Soraka': 'Enchanter',
 'Swain': 'Battlemage', 'Syndra': 'Burst', 'Tahm Kench': 'Warden',
 'Taliyah': 'Battlemage', 'Talon': 'Assassin', 'Taric': 'Enchanter',
 'Teemo': 'Specialist', 'Thresh': 'Catcher', 'Tristana': 'Marksman',
 'Trundle': 'Juggernaut', 'Tryndamere': 'Skirmisher', 'Twisted Fate': 'Burst',
 'Twitch': 'Marksman', 'Udyr': 'Juggernaut', 'Urgot': 'Juggernaut',
 'Varus': 'Marksman', 'Vayne': 'Marksman', 'Veigar': 'Burst',
 "Vel'Koz": 'Artillery', 'Vi': 'Diver', 'Viktor': 'Battlemage',
 'Vladimir': 'Battlemage', 'Volibear': 'Juggernaut', 'Warwick': 'Diver',
 'Wukong': 'Diver', 'Xayah': 'Marksman', 'Xerath': 'Artillery',
 'Xin Zhao': 'Diver', 'Yasuo': 'Skirmisher', 'Yorick': 'Juggernaut',
 'Zac': 'Vanguard', 'Zed': 'Assassin', 'Ziggs': 'Artillery',
 'Zilean': 'Specialist', 'Zoe': 'Burst', 'Zyra': 'Catcher'}
attribute_list = ['Enchanter','Catcher','Juggernaut','Diver','Burst',
'Battlemage','Artillery','Marksman','Assassin','Skirmisher','Vanguard',
'Warden','Specialist']

#convert samples into vector of champion counts
def vectorize_champ(sample):
    champ_list = list(champ_dic.keys())
    x = [0] * (len(champ_list) * 2)
    for champ in sample[:5]:
        x[champ_list.index(champ)] += 1
    for champ in sample[5:]:
        x[len(champ_list) + champ_list.index(champ)] += 1
    return np.array(x)

#convert samples (vector of length 10) into vector of attribute counts
#[ally 13 attributes][enemy 13 attributes]
def vectorize_attribute(sample):
    x = [0] * (len(attribute_list) * 2)
    #ally champions
    for champ in sample[0:5]:
        attribute = champ_dic[champ]
        x[attribute_list.index(attribute)] += 1
    #enemy champions
    for champ in sample[5:]:
        attribute = champ_dic[champ]
        x[len(attribute_list) + attribute_list.index(attribute)] += 1
    return np.array(x)
