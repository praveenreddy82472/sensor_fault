from Sensor.entity.config import TrainingPipelineConfig,DataIngestionConfig
from Sensor.entity.artifact import DataIngestionArtifact

from Sensor.exception import SensorException
import sys,os
from Sensor.logger import logging
from Sensor.components.data_ingestion import DataIngestion

class TrainPipeline:
    is_pipeline_running=False
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        #self.s3_sync = S3Sync()
        


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except  Exception as e:
            raise  SensorException(e,sys)
    
    def start_data_validaton():...
  

    def start_data_transformation():...
    
    def start_model_trainer():...
    def start_model_evaluation():...
    def start_model_pusher():...

    def sync_artifact_dir_to_s3(self):...
            
    def sync_saved_model_dir_to_s3(self):...
    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running=True

            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            
            raise SensorException(e,sys)