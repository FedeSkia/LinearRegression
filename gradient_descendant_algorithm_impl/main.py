import pandas as pd

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i,0] #represent studytime
        y = points.iloc[i,1] #represent score
        total_error += (y - (m * x + b)) ** 2
    return total_error / len(points)


def gradient_descendant(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i,0]
        y = points.iloc[i,1]
        m_gradient += -(2 / n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2 / n) * (y - (m_now * x + b_now))

    m = m_now - L * m_gradient
    b = b_now - L * b_gradient
    return m, b

df = pd.read_csv('data/data.csv')
df.columns = df.iloc[0]
df = df[0:] #remove the first line of the dataset

#print(loss_function(0, 1, df)) #assuming a parallel line with x axis
#print(loss_function(1, 1, df)) #assuming a parallel line with x axis

m = 0
b = 0
L = 0.0001
iterations = 10

for i in range(iterations):
    m, b = gradient_descendant(m, b, df, L)
    print(m, b)

print(m, b)