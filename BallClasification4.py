from sklearn import tree

def MarvellousClasifier():
    # Feature Encoding
    Feature = [[35,1], [47,1], [90,0], [48,1],[90,1], [35,1],[92,1],[35,1],[35,1],[35,1]]
    
    # Label Encoding
    Labels = [1,1,2,1,2,1,2,1,1,1]

    # Decide the model
    obj = tree.DecisionTreeClassifier()

    # train The model
    obj = obj.fit(Feature, Labels)

    ret = (obj.predict([[96,0]]))
    if ret == 1:
        print("Your object looks like Tennis Ball")
    else:
        print("Your object looks like Cricket Ball")

def main():
    print("--------Ball type Classification case study-----------")

    MarvellousClasifier()

if __name__ == "__main__":
    main()

# Data set Size : 15
# Training Size : 10
# Testing Size  : 5