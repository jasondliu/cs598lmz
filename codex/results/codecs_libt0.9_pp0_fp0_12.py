import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Special directory imports
sys.path.append(os.getcwd() + '\\modules')

import d2xx
import time
import msvcrt
import binascii
import itertools
import math
from tqdm import tqdm

################################################################
# DSI functions
dsiOriginIdentify = {'LEFT':0x1d, 'CENTER':0x1e, 'RIGHT':0x1f}
dsiHorizontalPattern = {'NONE':0, 'LOW':1, 'HIGH':2, 'STARS':3, 'DOTS':4}
dsiVerticalPattern = {'NONE':0, 'LOW':1, 'HIGH':2, 'STARS':3, 'DOTS':4}

def dsiStart(handle):
    handle.writeData(b'\x04\x01')

def dsiSendPattern(handle, left, right, vertical, horizontal, brightness = None,
