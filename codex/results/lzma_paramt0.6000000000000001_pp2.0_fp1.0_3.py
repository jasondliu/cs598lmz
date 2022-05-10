from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

print(data)

'''

import lzma
import csv
import sys
import os
import re
import datetime

import logging
logging.basicConfig(filename='logs/log_'+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.txt',level=logging.DEBUG)

logging.info('Started')

def get_file_name(file_path):
    return file_path.split('/')[-1]

def get_file_extension(file_path):
    return file_path.split('.')[-1]

def get_file_name_no_extension(file_path):
    return get_file_name(file_path).split('.')[0]

def get_file_path_no_extension(file_path):
    return file_path[:-len(get_file_name(file_path))]

def get_file_path_no_name(file
