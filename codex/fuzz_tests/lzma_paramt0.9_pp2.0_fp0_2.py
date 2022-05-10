from lzma import LZMADecompressor
LZMADecompressor
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import numpy as np
import pickle

#download training data
#url="http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
#print(requests.get(url).status_code)
#r = requests.get(url, allow_redirects=True)
#open('train-images-idx3-ubyte.gz','wb').write(r.content)

#load training data images
train_data = []
with gzip.open('train-images-idx3-ubyte.gz', 'rb') as f:
	x = f.read(16)
	assert x[0:4] == b'\x00\x00\x08\x03'
	channels = x[4]
	assert x[5] == 0
	height = int.from_bytes(x[6:10], signed=False)
	width = int
