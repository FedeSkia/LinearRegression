''' Is price dependant on the number of reviews?'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/listings.csv')

df_reviews_price = df[['number_of_reviews', 'price']]

plt.scatter(df_reviews_price.number_of_reviews, df_reviews_price.price)
#plt.show() #seems like no correlation exists

'''  split test and train datasets'''
train, test = train_test_split(df, test_size=0.2)

''' create 2 one dimensional array where train_x is the reviews and train_y is the prices.
 These will be used to train the model '''
train_x = np.reshape(train.number_of_reviews, (-1, 1)) # #reviews
train_y = np.reshape(train.price, (-1, 1))             # prices

model = LinearRegression()
model.fit(train_x, train_y)

''' create 2 one dimensional array where test_x is the reviews and test_y is the prices.
 These will be used to validate the model '''
test_x = np.reshape(test.number_of_reviews, (-1, 1))
test_y = np.reshape(test.price, (-1, 1))

prediction = model.predict(test_x)

print(model.score(test_y, prediction))

plt.scatter(train_x, train_y, color='g')
plt.plot(test_x, prediction, color='k')
plt.show()

''' Can conclude that there's no relationship between the twos '''