''' Letes verify if there s a correlation between price and beds number of bathroom'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df = pd.read_csv('data/American_Housing_Data_20231209.csv')

df_interesting_columns = df[['Beds', 'Baths', 'Price']]

independent_variables = df_interesting_columns[['Beds', 'Baths']]
dependent_variable = df_interesting_columns[['Price']]

X_train, X_test, y_train, y_test = train_test_split(independent_variables, dependent_variable, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

r_squared = model.score(X_test, y_test)
#or
r2_score = r2_score(y_test, predictions)
print(r2_score)


# Scatter plot of actual vs predicted values
predictions.plot()

plt.scatter(y_test, predictions)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs Predicted Prices")
plt.show()
# Overlay the regression line
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', linewidth=2, label='Perfect Fit')
plt.legend()

plt.show()