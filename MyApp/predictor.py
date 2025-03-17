
import pickle
import pandas as pd
import sklearn.pipeline as skp
from typing import cast

class Predictor():
    def __init__(self, filename:str):
        self.filename = filename
        self.pipeline = None
        self.load_pipeline()

    def load_pipeline(self) :
        serialized_object = None
        with open(self.filename, 'rb') as reading_file:
            serialized_object = pickle.load(reading_file)

        self.pipeline = cast(skp.Pipeline,serialized_object )

    def predict(self,  age : int, sex: str, bmi: float, children : int, smoker: str, region: str ) -> int: 
       
        data = [[age, sex, bmi, children, smoker, region]]
        X = pd.DataFrame(data, columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

        y = self.pipeline.predict(X)   
        #single_prediction = cast (float, y[0])
        single_prediction = int(y[0])

        return single_prediction




