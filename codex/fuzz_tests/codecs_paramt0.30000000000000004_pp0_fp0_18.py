import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import json
import time
import random
import datetime
import logging
import logging.handlers
import traceback
import subprocess

import requests
import requests.exceptions
import requests.packages.urllib3

import config
import utils

requests.packages.urllib3.disable_warnings()

logger = logging.getLogger('bot')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh = logging.handlers.TimedRotatingFileHandler(config.LOG_FILE, when='midnight', backupCount=7)
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
log
