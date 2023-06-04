import numpy as np
import pandas as pd
import pickle
import json
import warnings
warnings.filterwarnings("ignore")
import config
class FloType():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm=SepalLengthCm
        self.SepalWidthCm=SepalWidthCm
        self.PetalLengthCm=PetalLengthCm
        self.PetalWidthCm=PetalWidthCm
  
    
    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data=json.load(f)     

    def get_predicted(self):
        
        self.load_models()  
        
        test_array=np.zeros(len(self.json_data["columns"]))
       
        test_array[0]=self.SepalLengthCm
        test_array[1]=self.SepalWidthCm
        test_array[2]=self.PetalLengthCm
        test_array[3]=self.PetalWidthCm
        print("test array -->\n",test_array)
        charges=round(self.model.predict([test_array])[0],2) 
        return charges
if __name__== "__main__":
    SepalLengthCm=5.1
    SepalWidthCm=3.5
    PetalLengthCm=1.4
    PetalWidthCm=0.2
    
    
    flo_pri=FloType(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    premium=flo_pri.get_predicted()
    print("Predicted Prices:",premium,"/-rs")        


