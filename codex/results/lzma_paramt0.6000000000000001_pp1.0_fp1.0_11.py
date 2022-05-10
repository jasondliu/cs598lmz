from lzma import LZMADecompressor
LZMADecompressor.__module__ = 'lzma'

import sys
import os.path
import urllib.request
import json
import argparse
import re
import struct
import shutil
import socket
import threading
import time

def get_platform():
    if sys.platform.startswith('win'):
        return 'windows'
    elif sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform.startswith('darwin'):
        return 'osx'
    else:
        return sys.platform

class Version(object):
    def __init__(self, version):
        self.version = version
        self.major = None
        self.minor = None
        self.patch = None
        self.release = None
        self.build = None
        self.qualifier = None
        self.snapshot = False

        m = re.match('^(\d+)\.(\d+)\.(\d+)(?:-([a-zA-Z0-9]+))?(?:\+([0-
