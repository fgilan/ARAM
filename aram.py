import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#dictionary of champions and their attributes
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

df = pd.read_csv("game_data_2.csv", encoding='utf-8')
#encode win/losses
win_lose = df.iloc[:,0].values
le = LabelEncoder()
y1 = le.fit_transform(win_lose)
#game length in seconds
y2 = df.iloc[:,1].values
#champion data
champs = df.iloc[:,2:].values

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

#predict
def predict_outcome(champs):
    input = vectorize_champ(champs).reshape(1,-1)
    outcome = log_reg.predict(input)[0]
    length = lin_reg.predict(input)[0]
    if outcome == 0:
        print("Defeat")
    else:
        print("Victory")
    print("{} m {} s".format(length//60, length%60))

#vectorize input data
X = []
for sample in champs:
    X.append(vectorize_champ(sample))
X = np.array(X)
#Logisitic Regression on wins/losses
#split into train and test sets
X_train, X_test, y1_train, y1_test = train_test_split(X, y1,
                                                    test_size = 0.4,
                                                    stratify = y1,
                                                    random_state = 1)
log_reg = LogisticRegression(random_state=1)
log_reg.fit(X_train, y1_train)
print('W/L Training Accuracy: %.3f' % log_reg.score(X_train, y1_train))
print('W/L Test Accuracy: %.3f' % log_reg.score(X_test, y1_test))
#Linear regression on game Length
X_train, X_test, y2_train, y2_test = train_test_split(X, y2,
                                                    test_size=0.1,
                                                    random_state=1)
lin_reg = LinearRegression()
lin_reg.fit(X_train, y2_train)
y2_train_pred = lin_reg.predict(X_train)
y2_test_pred = lin_reg.predict(X_test)
print('Training MSE: %.3f' % mean_squared_error(y2_train, y2_train_pred))
print('Test MSE: %.3f' % mean_squared_error(y2_test, y2_test_pred))
