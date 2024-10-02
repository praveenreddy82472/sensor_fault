from Sensor.configuration.mongo_db_connection import MongoDBClient
from Sensor.entity.config import TrainingPipelineConfig,DataIngestionConfig
from Sensor.pipeline.training_pipeline import TrainPipeline
if __name__ == '__main__':
    train_pipeline=TrainPipeline()
    train_pipeline.run_pipeline()