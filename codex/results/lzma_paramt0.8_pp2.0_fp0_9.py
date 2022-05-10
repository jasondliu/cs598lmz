from lzma import LZMADecompressor
LZMADecompressor().decompress(b1)

# -*- coding: utf-8 -*-
import base64
import datetime
import hashlib
import json
import logging
import os
import random
import time

import requests

# 日志
logger = logging.getLogger("b2c")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# 应用根目录
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\"

# 公共参数
DEVICE_UUID = 'ffffffff-d1c6-c6b8-ffff-ffffd1acf040'
DEVICE_TYPE = 'Android'
DEVICE_MODEL = 'vivo-1714'
APP_VERSION = '4.3.3'
APP_VERSION_CODE = '433'
APP_CHANN
