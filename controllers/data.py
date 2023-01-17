import os
import pickle

class DataWorker:
    def __init__(self):
        with open(os.path.join('/src/models_dump/', 'data'), 'rb') as f:
            self.data = pickle.load(f)
    
    def get_sample(self):
        feature_cols = list(self.data.columns)
        feature_cols = [col for col in feature_cols if col != 'BioSample' and col != 'target' and col != 'Region']
        return self.data.sample(n=1)[feature_cols]