import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import os
import sys
import platform
import argparse
import subprocess
import re
import datetime
import time
from datetime import datetime, timedelta
import logging
from logging.handlers import RotatingFileHandler
from shutil import copyfile
import requests
import json
import socket

parser = argparse.ArgumentParser(description='Run the ai4eutils tests')
parser.add_argument('--test-dir', required=True, dest='test_dir', help='The test directory')
parser.add_argument('--test-file', required=True, dest='test_file', help='The test file')
parser.add_argument('--test-name', required=True, dest='test_name', help='The test name')
parser.add_argument('--test-result', required=True, dest='test_result', default='Test failed', help='The test result')
parser.add_argument('--test-message', required=True, dest='test_message',
