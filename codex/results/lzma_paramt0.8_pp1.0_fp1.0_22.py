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

from sitescripts.extensions.models import Extension
from sitescripts.utils import get_config


def get_extension_id(extension, version):
    # From https://developer.chrome.com/extensions/crx
    # The public key is a base64-encoded string of the public key.
    # The ID is a unique id for this extension, based on the public key.
    # To generate the ID of an extension, take the SHA-256 hash of the
    # public key, and return the hash in hex. The first 32 characters of the
    # hash are used.
    # https://developer.chrome.com/webstore/inline_installation#id
