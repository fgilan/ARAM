import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import shared

df = pd.read_csv("game_data_2.csv", encoding='utf-8')
#encode win/losses
win_lose = df.iloc[:,0].values
le = LabelEncoder()
y1 = le.fit_transform(win_lose)
#game length in seconds
y2 = df.iloc[:,1].values
#champion data
champs = df.iloc[:,2:].values
#vectorize input data
X = []
for sample in champs:
    X.append(shared.vectorize_attribute(sample))
X = np.array(X)
#Logisitic Regression on wins/losses
#split into train and test sets
X_train, X_test, y1_train, y1_test, y2_train, y2_test = train_test_split(X, y1, y2,
                                                    test_size = 0.4,
                                                    stratify = y1,
                                                    random_state = 1)
#Save the vectorized data so we don't have to keep reading the file
np.savez_compressed('vectorized_data.npz',
    X_train = X_train, y1_train = y1_train, y2_train = y2_train,
    X_test = X_test, y1_test = y1_test, y2_test = y2_test)
