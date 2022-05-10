from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor

import os
import pprint
import re
import socket
import sys
import time
import urllib
def quote(s):
    return urllib.parse.quote_plus(s)

sys.path.append(os.path.join(os.path.dirname(__name__), '..', '..', '..'))

import requests

