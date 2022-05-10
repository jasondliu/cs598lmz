import mmap
import gc
import os
import kaggle_util
import torch

def convert_data():
    dtypes = {
        'ip': 'uint32',
        'app': 'uint16',
        'device': 'uint16',
        'os': 'uint16',
        'channel': 'uint16',
        'is_attributed': 'uint8',
        'click_id': 'uint32'
    }

    print('loading train data...')
    train_path = 'C:\\Users\\Samuel\\Documents\\GitHub\\kaggle_talkingdata_fraud_detection\\data\\train_sample.csv'
    usecols = ['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed']
    train_df = pd.read_csv(train_path, dtype=dtypes, usecols=usecols)

    print('loading test data...')
    test_path = 'C:\\Users\\Samuel\\Documents\\GitHub\\kaggle_talkingdata_fraud_
