import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    
    # Load data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    
    print("Values of Independent of variables x",X)
    print("Values of Dependent of variables y",Y)
    
    # Least Square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    
    print("Mean of Independent variable x",mean_x)
    print("Mean of Dependent variable y",mean_y)
    n = len(X)

    numerator = 0
    denomenator = 0
    
    # Equation of line is y = mx + c

    for i in range(n):
        numerator = numerator + (X[i] -mean_x)*(Y[i] - mean_y)
        
        denomenator =  denomenator + (X[i] - mean_x)**2

    m = numerator / denomenator

    # c = y' - mx'

    c = mean_y - (m * mean_x)

    print("Slope of Regression line is",m)          # 0.4
    print("Y intercept of Regression line is",c)    # 2.4

    # Display plotting of above points
    x = np.linspace(1,6,n)

    y = c + m * x

    plt.plot(x,y, color='#58b970', label='Regression Line')

    plt.scatter(X,Y, color='#ef5423' ,label='scatter plot')
    # plt.scatter(X,y_pred, color='blue' ,label='scatter plot')

    plt.xlabel('X - Independent Variable')
    plt.ylabel('Y - Dependent Variable')

    plt.legend()
    plt.show()

    # Findout goodness of fit ie R Square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m *X[i]
        ss_t += (Y[i] - mean_y) ** 2
        ss_r += (Y[i] - y_pred) ** 2

    r2 = 1 - (ss_r/ss_t)

    print("Goodness of fit using R2 methos is",r2)

def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")
    
    print("Suervised Machine Learning")
    
    print("Linear Regreesion")
    
    MarvellousPredictor()

if __name__ == "__main__":
    main()
