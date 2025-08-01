# Step 6

import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass # used to create class variable

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer



# step 6.1 class
@dataclass
class DataIngestionConfig:
    # Inputes
    train_data_path : str = os.path.join("artifacts","train.csv") # all the output will store in articacts folder
    test_data_path : str = os.path.join("artifacts","test.csv")
    raw_data_path : str = os.path.join("artifacts","raw_data.csv")



# step 6.2 
class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    # It used to read the data from data bases
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            # only 'Notebook\data\StudentsPerformance.csv' this will changed . all this code will same
            # it can be api, from UI..anywhere
            df = pd.read_csv(r'Notebook\data\StudentsPerformance.csv') 

            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2 ,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)




if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # Data Transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # Model Training
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
