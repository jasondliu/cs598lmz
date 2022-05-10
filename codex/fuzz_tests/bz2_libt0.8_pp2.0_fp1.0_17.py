import bz2
bz2.BZ2File('amazon_reviews_us_Digital_Video_Download_v1_00.tsv.bz2')

#%%
import json
import boto3
filename='Upwork_transactions_2020_01_Clean.csv'
s3_resource=boto3.resource('s3')
s3_resource.Object('gloria-lai-bucket','Upwork_transactions_2020_01_Clean.csv')\
.upload_file(filename)
#%%
import boto3
import sagemaker
from sagemaker import get_execution_role

session = sagemaker.Session()
bucket = session.default_bucket()  
prefix = 'sagemaker/DEMO-xgboost-dm'

role = get_execution_role()
import pandas as pd
import io
import boto3
import os
import sys
import time

#%%
data_key = 'Upwork_transactions_2020_01_Clean.csv'
data_location = 's3://gloria-lai-bucket/
