# step 8

#  fetch the data from the data base
import os
import sys 
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException



# step through ---->7.3 only method
def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)
