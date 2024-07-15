import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def TitanicLogistic():
    # Step 1 : Load the data from CSV
    titanic_data = pd.read_csv("Machine_Learning\TitanicDataset.csv")

    print("First 5 entries from loaded data set")
    print(titanic_data.head())

    print("Number of Passangers are " + str(len(titanic_data)))

    # Step 2 : Analyze the data
    print("Visualisation : Survived and non survived passangers")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x=target).set_title("Survived and non survived passangers")
    show()

    print("Visualisation : Survived and non survived passangers based on gender")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x=target, hue="Sex").set_title("Survived and non survived passangers based on gender")
    show()

    print("Visualisation : Survived and non survived passangers based on the passanger class")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x=target, hue="Pclass").set_title("Survived and non survived passangers based on the passanger class")
    show()

    print("Visualisation : Survived and non survived passangers based Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Survived and non survived passangers based on Age")
    show()

    print("Visualisation : Survived and non survived passangers based on the Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Survived and non survived passangers based on Fare")
    show()

    # Step 3 : data Cleaning
    titanic_data.drop("zero", axis = 1, inplace = True)

    print("First 5 entries from loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("Values of Sex Column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of sex column after removing one feild")
    Sex = pd.get_dummies(titanic_data["Sex"],drop_first = True)
    print(Sex.head(5))

    print("Values of Plass column after removing one feild")
    Pclass = pd.get_dummies(titanic_data["Pclass"],drop_first = True)
    print(Pclass.head(5))

    print("Values of dataset after concatenating new columns")
    titanic_data = pd.concat([titanic_data,Sex,Pclass],axis = 1)
    print(titanic_data.head(5))

    print("Values of data set after removing irrelevent coluns")
    titanic_data.drop(["Sex", "sibsp", "Parch", "Embarked"], axis = 1, inplace = True)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived", axis = 1)
    y = titanic_data["Survived"]

    # Step 4 : Data Trainig

    xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.5)

    logmodel = LogisticRegression()

    logmodel.fit(xtrain, ytrain)

    # Step 5 : Data Testing
    prediction = logmodel.predict(xtest)

    # Step 5 : Calculate Accuracy
    print("Classification report of Logistic Regression : ")
    print(classification_report(ytest, prediction))

    print("Confussion matrix of Logistic Regression is : ")
    print(confusion_matrix(ytest, prediction))

    print("Accuracy of Logistic Regression is : ")
    print(accuracy_score(ytest, prediction))

def main():
    print("---------------------Created By Mahesh Pawar----------------------")

    print("Supervised Machine Learning")

    print("Logistic Regression on Titanic data set")

    TitanicLogistic()

if __name__ == "__main__":
    main()