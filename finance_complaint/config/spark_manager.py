# from finance_complaint.constant.environment.variable_key import AWS_ACCESS_KEY_ID_ENV_KEY,AWS_SECRET_ACCESS_KEY_ENV_KEY

import os
from pyspark.sql import SparkSession
# access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY, )
# secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY, )


spark_session = SparkSession.builder.master('local[*]').appName('finance_complaint').getOrCreate()
    