import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def HeadBrainPredictor():
    # Load the data
    data = pd.read_csv('Machine_Learning\HeadBrain.csv')
    print("Size of data set",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    # Least Square Method
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    n = len(X)

    numerator = 0
    denomenator = 0

    # Equation of line is Y = mX + c
    for i in range(n):
        numerator = numerator + (X[i]-mean_X)*(Y[i]-mean_Y)
        denomenator = denomenator + (X[i]-mean_X) ** 2

    m = numerator / denomenator

    c = mean_Y - (m * mean_X)

    print("Slope of Regression line is ",m)
    print("Y intersects of Regression line is ",c)

    max_x = np.max(X)+100
    min_x = np.min(X)-100

    # Display Ploting of above points
    x = np.linspace(min_x,max_x,n)

    y = m*x + c

    plt.plot(x,y, color = '#58b970', label = 'Regression line')
    plt.scatter(X, Y, color = '#ef5423', label = 'Scatter plot')

    plt.xlabel('Head Size(cm^3)')
    plt.ylabel('Brain Weight in grams')

    plt.legend()
    plt.show()

    # Findout goodness of fit in R Square
    numerator = 0
    denomenator = 0
    for i in range(n):
        y_pred = c + m*X[i]
        numerator = numerator + (Y[i]-mean_Y)**2
        denomenator = denomenator + (Y[i]-y_pred) ** 2

    r2 = 1 - (numerator / denomenator)

    print(r2)

def main():
    print("----------------Created By Mahesh Pawar---------------")

    print("Supervised Machine Learning")

    print("Linear Regression on Head and Brain size data set")
    print("------------------------------------------------------")

    HeadBrainPredictor()

    print("------------------------------------------------------")

if __name__ == "__main__":
    main()