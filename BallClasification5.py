from sklearn import tree

def MarvellousClasifier(weight, surface):
    # Feature Encoding
    Feature = [[35,1], [47,1], [90,0], [48,1],[90,1], [35,1],[92,1],[35,1],[35,1],[35,1]]
    
    # Label Encoding
    Labels = [1,1,2,1,2,1,2,1,1,1]

    # Decide the model
    obj = tree.DecisionTreeClassifier()

    # train The model
    obj = obj.fit(Feature, Labels)

    ret = (obj.predict([[weight,surface]]))
    if ret == 1:
        print("Your object looks like Tennis Ball")
    else:
        print("Your object looks like Cricket Ball")

def main():
    print("--------Ball type Classification case study-----------")

    print("Please enter the information about the object  that you want to test")
    
    print("Please enter weight of your object in grams")
    no = int(input())

    print("Please mention the type of surface Rough/Smooth")
    data = (input())

    if data.lower() == "rough":
        data = 1
    elif data.lower() == "smooth":
        data = 0
    else:
        print("Invalid type of surface")
        exit()

    MarvellousClasifier(no,data)

if __name__ == "__main__":
    main()

# Data set Size : 15
# Training Size : 10
# Testing Size  : 5