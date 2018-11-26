import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import shared

#load data
vectorized_data = np.load('vectorized_data.npz')
X_train, y1_train, y2_train, X_test, y1_test, y2_test = \
    [vectorized_data[x] for x in vectorized_data.files]

#predict
def predict_outcome(champs):
    input = shared.vectorize_champ(champs).reshape(1,-1)
    outcome = log_reg.predict(input)[0]
    length = lin_reg.predict(input)[0]
    if outcome == 0:
        print("Defeat")
    else:
        print("Victory")
    print("{} m {} s".format(length//60, length%60))

#Regression on win/loss
log_reg = LogisticRegression(random_state=1)
log_reg.fit(X_train, y1_train)
print('W/L Training Accuracy: %.3f' % log_reg.score(X_train, y1_train))
print('W/L Test Accuracy: %.3f' % log_reg.score(X_test, y1_test))

#Linear regression on game Length
lin_reg = LinearRegression()
lin_reg.fit(X_train, y2_train)
y2_train_pred = lin_reg.predict(X_train)
y2_test_pred = lin_reg.predict(X_test)
print('Training MSE: %.3f' % mean_squared_error(y2_train, y2_train_pred))
print('Test MSE: %.3f' % mean_squared_error(y2_test, y2_test_pred))
