from sklearn import tree

# Rough 1
# Smmoth 0

# Tennis 1
# Cricket 2
def main():
    print("Ball Classification Case study")

    # Feature Encoding
    Feature = [[35,1], [47,1], [90,0], [48,1],[90,1], [35,1],[92,1],[35,1],[35,1],[35,1]]
    
    # Label Encoding
    Labels = [1,1,2,1,2,1,2,1,1,1]

    # Decide the model
    obj = tree.DecisionTreeClassifier()

    # train The model
    obj = obj.fit(Feature, Labels)

    print(obj.predict([[96,0]]))
    print(obj.predict([[43,1]]))

if __name__ == "__main__":
    main()

# Data set Size : 15
# Training Size : 10
# Testing Size  : 5