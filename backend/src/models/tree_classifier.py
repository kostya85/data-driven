import os
import pickle
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

class TreeClassifier:
    class_mapping = {1: "HEALTH", 0: "DIABETES", 2: "OBESITY"}

    def __init__(self):
        with open(os.path.join('/src/models_dump/', 'tree_classifier'), 'rb') as f:
            self.model: DecisionTreeClassifier = pickle.load(f)

    def predict(self, data):
        result = self.model.predict(data)
        predict_proba = self.model.predict_proba(data)
        accuracy = {name: result for name, result in zip(data.index.values.tolist(), predict_proba)}
        return {'class' : self.class_mapping[result[0]], 'accuracy': accuracy[data.index.values.tolist()[0]][result[0]]}