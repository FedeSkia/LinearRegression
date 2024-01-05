import pandas as pd

df = pd.read_csv('data/olympics.csv', skiprows=4)

#Shape returns a tuple representing rows and columns represting the dimensionality of the dataframe
#print("shape is ", df.shape) #(number of rows, number of columns)
#print("number of rows", df.shape[0])
#print("number of columns", df.shape[1])

#Head and tail returns respectively the first 5 rows and the last 5 rows
#print(df.head())
#print(df.tail())

#info provides useful info about the data set like null values, type of object
#print(df.info())

#value_counts() count of unique values
#print(df.value_counts())
#print(df.Gender.value_counts()) # it will return the unique values of the series

#sort_values sort valuess in a series or ina dataframe
#sort by the athletes name
ath = df.Athlete.sort_values()
#sort by Edition first then Athlete
#print(df.sort_values(by=['Edition', 'Athlete']))

#Boolean indexing
#print(df.Medal == 'Gold')
#if you want to filter by all the medal == gold and being women but having the dataframe
#print(df[ (df.Medal == 'Gold') & (df.Gender == 'Women')])

#String handling
#Access values of series and check the string values
#print(df.Athlete[df.Athlete.str.contains('Florence')].head())


#Challenge 1 in which events did Jesse Owens win a medal
#print(df.Edition[ df.Athlete == 'OWENS, Jesse' ])

#Which country has won the most mens gold medal in single badmintons over the year?

#df_with_man_and_badminton = df[ (df.Sport == 'Badminton') & (df.Gender == 'Men') & (df.Medal == 'Gold') & (df.Event == 'singles')]
#print(df_with_man_and_badminton.count())

#Which country have won the most medals in recent years?
#print(df[df.Edition > 1984].NOC.value_counts().head(3))

#Display the gold medal winners for the 100m Track and field  sprint over the years. List the results starting with the most recent
freestyle = df[ (df.Event == '100m freestyle') & (df.Medal ==  'Gold') ]
#print(freestyle.sort_values(by=['Edition']))

import matplotlib.pyplot as plt
#PLOT

#Different kind of plots
'''
plt.plot(kind = 'line', color = 'blue')
plt.plot(kind = 'bar')
plt.plot(kind = 'barh')
plt.plot(kind = 'pie')
'''


#you can use plot chaining it on the dataframe like
#df.Sport.value_counts().plot(kind = 'bar', color = 'red')
#plt.show()

#SEABORN creates plot and works well with pandas
#you want to use seaborn for more advanced plots
import seaborn as sns

#sns.countplot(x='Medal', data=df, hue='Gender') #it takes the x attribute from the dataframe

#Exercise
#Plot the number of medals achieved by the Chinese team (men and women) in Beijing 2008
#b_CHN = df[ (df.City == 'Beijing') & (df.NOC == 'CHN') ]
#men_women_won_plot = b_CHN['Gender'].value_counts().plot(kind = 'bar')
#plt.show()

#sns.countplot(x = 'Gender', data=b_CHN, palette='bwr')
#plt.show()

#gender_medal_value_counts = b_CHN[['Gender', 'Medal']]
#sns.countplot(x='Medal', data=df, hue='Gender', palette='dark:red')
#plt.show()

#Index it is an immutable array and allow to access a row or column using label
#it is the first column of the dataframe
#df.index[100] #will return 100
#you can set the index to be one of the column of the dataframe
#df.set_index('Athlete', inplace=True) #will set the athlete column to be the index
#df.reset_index(inplace=True) #To reset the index
#sort_index will sort the dataframe according to the index

#loc[]  DataFrame.loc[] / DataFrame.Series.loc[] allow to select by label by the index
#df.loc['Bolt, Usain']

#iloc uses integer
#df.iloc[1700]
#df.iloc[[1542, 2390, 6000, 15000]] #return the rows corresponding to the index specified
#df.iloc[1:4] #return the rows from 1 to 4
'''
df['Edition'].value_counts().plot(kind = 'bar')
#plt.show()
all_countries = df['NOC'].drop_duplicates()
edition2008 = df[df.Edition == 2008]
countries_edition_2008 = edition2008['NOC']

#remove from countries all from edition2008
countries_not_present_in_2008 = countries_edition_2008.isin(all_countries.NOC)
'''

#group by
#df.groupby('Edition') #returns a dataframe for each edition
df.set_index('Edition', inplace=True)
df.sort_values(by='Edition')
#print(df.groupby('Edition').size()) #it is a count
df.reset_index()
print(df.groupby(['Edition', 'NOC']).agg(['min','max','count']))
