import lzma
lzma_path = '/Users/nicholas/Documents/thesis/binaries/lzma.so'
sys.path.append(lzma_path)
import lzma
import json
import requests
import time
import pickle
import os
import numpy as np
from tqdm import tqdm

# get json from url
def get_json(url):
    response = requests.get(url)
    try:
        data = response.json()
    except json.decoder.JSONDecodeError:
        data = response.status_code
    return data

# decode the compressed json
def decode_json(data):
    data = lzma.decompress(data)
    data = json.loads(data)
    return data

# get an object from the url
def get_obj(url):
    data = get_json(url)
    if type(data) is int:
        return data
    else:
        data = decode_json(data)
        return data

# get obj from the url and save it to the path
def
