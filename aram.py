import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#get up to date list of champions
champ_list = ['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia',
'Annie', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank', 'Brand',
'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath", 'Corki', 'Darius',
'Diana', 'Dr. Mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal',
'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar',
'Gragas', 'Graves', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern',
'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista',
'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen',
"Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin', 'Leona',
'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai',
'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus',
'Nautilus', 'Nidalee', 'Nocturne', 'Nunu & Willump', 'Olaf', 'Orianna',
'Ornn', 'Pantheon','Poppy','Pyke','Quinn','Rakan','Rammus',"Rek'Sai",
'Renekton','Rengar','Riven','Rumble','Ryze','Sejuani','Shaco','Shen',
'Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain',
'Syndra','Tahm Kench', 'Taliyah', 'Talon','Taric','Teemo','Thresh',
'Tristana','Trundle','Tryndamere','Twisted Fate','Twitch','Udyr',
'Urgot','Varus','Vayne','Veigar',"Vel'Koz",'Vi','Viktor','Vladimir','Volibear',
'Warwick','Wukong','Xayah','Xerath','Xin Zhao','Yasuo','Yorick','Zac',
'Zed','Ziggs','Zilean','Zoe','Zyra']


df = pd.read_csv("game_data.csv", encoding='utf-8')
#encode win/losses
win_lose = df.iloc[:,0].values
le = LabelEncoder()
y1 = le.fit_transform(win_lose)
#game length in seconds
y2 = df.iloc[:,1].values
#champion data
champs = df.iloc[:,2:].values

#convert samples (vector of length 10) into one-hot vector
#[player 1][ally 4][enemy 5]
def vectorize(sample):
    x = [0] * (len(champ_list) * 3)
    #player champion
    player_champion = sample[0]
    idx = champ_list.index(player_champion)
    x[idx] = 1
    #ally champions
    for champ in sample[1:5]:
        idx = champ_list.index(champ)
        x[len(champ_list) + idx] = 1
    #enemy champions
    for champ in sample[5:]:
        idx = champ_list.index(champ)
        x[len(champ_list) * 2 + idx] = 1
    return x

#vectorize input data
X = []
for champ in champs:
    X.append(vectorize(champ))
X = np.array(X)
#Logisitic Regression on wins/losses
#split into train and test sets
X_train, X_test, y1_train, y1_test = train_test_split(X, y1,
                                                    test_size = 0.1,
                                                    stratify = y1,
                                                    random_state = 1)
lr = LogisticRegression(C=100, random_state = 1)
lr.fit(X_train, y1_train)
print('W/L Training Accuracy: %.3f' % lr.score(X_train, y1_train))
print('W/L Test Accuracy: %.3f' % lr.score(X_test, y1_test))
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
