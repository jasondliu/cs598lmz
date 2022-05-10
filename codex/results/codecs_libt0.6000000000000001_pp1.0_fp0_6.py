import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
import argparse
import json
import logging
import re
import os
import shutil

from utils import *

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--logging-level', help='Logging level')
    parser.add_argument('-f', '--logging-file', help='Logging file name')
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    setup_logging(args.logging_level, args.logging_file)
    logger = logging.getLogger(os.path.basename(__file__))

    # with open('/Users/shiqichan/Desktop/test_data/test_data.json') as json_file:
    #     data = json.load(json_file)
    #     for item in data:
    #         print(item
