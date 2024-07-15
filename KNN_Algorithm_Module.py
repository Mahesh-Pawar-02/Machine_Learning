from scipy.spatial import distance

class Marvellous_KNN():
    def euc(a,b):
        return distance.euclidean(a,b)
    
    def fit(self, TrainingData, TrainingTarget):
        self.TrainigData = TrainingData
        self.TrainigTarget = TrainingTarget

    def predict(self, TestData):
        predictions = []
        for row in TestData:
            lebel = self.closest(row)
            predictions.append(lebel)
        return predictions
    
    def closest(self,row):
        bestdistance = euc(row, self.TrainigData[0])
        bestindex = 0
        for i in range(1, len(self.TrainigData)):
            dist = euc(row, self.TrainigData[i])
            if dist < bestdistance:
                bestdistance = dist
                bestindex = i
        return self.TrainigTarget[bestindex]