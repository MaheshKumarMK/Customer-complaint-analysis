
from finance_complaint.pipeline.training import TrainingPipeline
from finance_complaint.config.pipeline.training import FinanceConfig

if __name__ =="__main__":
    finance_config = FinanceConfig()
    training_pipeline = TrainingPipeline(finance_config = finance_config)
    training_pipeline.start()


