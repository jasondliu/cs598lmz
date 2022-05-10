import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import json
import pandas as pd

def get_data(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)

    return data

def get_all_data(file_name):
    with open(file_name) as f:
        content = f.readlines()

    return content

def get_pandas_dataframe(file_name):
    with open(file_name) as f:
        df = pd.read_json(f, orient='split')

    return df

def get_pandas_dataframe_from_string(data):
    df = pd.read_json(data, orient='split')

    return df

def get_json_from_string(data):
    return json.loads(data)
