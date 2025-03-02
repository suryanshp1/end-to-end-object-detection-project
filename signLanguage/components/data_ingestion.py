import sys
import os
from six.moves import urllib
import zipfile
from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.entity.artifacts_entity import DataIngestionArtifact
from signLanguage.logger import logging
from signLanguage.exception import SignLangException

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SignLangException(e, sys) from e
        
    def download_data(self) -> str:
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = os.path.basename(dataset_url)
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f'Downloading data from {dataset_url} to {zip_file_path}')
            urllib.request.urlretrieve(dataset_url, zip_file_path)
            logging.info(f'Data downloaded successfully at {zip_file_path}')
            return zip_file_path
        except Exception as e:
            raise SignLangException(e, sys) from e
        
    def extract_zip_file(self, zip_file_path: str):
        try:
            raw_data_dir = self.data_ingestion_config.feature_store_file_path
            os.makedirs(raw_data_dir, exist_ok=True)
            logging.info(f'Extracting zip file: {zip_file_path} into dir: {raw_data_dir}')
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(raw_data_dir)
            logging.info(f'Extraction completed')
            return raw_data_dir
        except Exception as e:
            raise SignLangException(e, sys) from e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info('Initiating data ingestion')
        zip_file_path = self.download_data()
        feature_store_path = self.extract_zip_file(zip_file_path)

        data_ingestion_artifact = DataIngestionArtifact(zip_file_path, feature_store_path)

        logging.info('Data ingestion completed')
        logging.info(f'Data Ingestion Artifact: {data_ingestion_artifact}')

        return data_ingestion_artifact
    

