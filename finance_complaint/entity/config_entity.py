from collections import namedtuple
from finance_complaint.constant.prediction_pipeline_config.file_config import ARCHIVE_DIR, FAILED_DIR, INPUT_DIR, \
    PREDICTION_DIR, REGION_NAME

TrainingPipelineConfig = namedtuple("PipelineConfig", ["pipeline_name", "artifact_dir"])

DataIngestionConfig = namedtuple("DataIngestionConfig", ["from_date",
                                                         "to_date",
                                                         "data_ingestion_dir",
                                                         "download_dir",
                                                         "file_name",
                                                         "feature_store_dir",
                                                         "failed_dir",
                                                         "metadata_file_path",
                                                         "datasource_url"
                                                         ])