import _struct
import os
import struct
import math
import sys


def decode_number(number):
    return struct.unpack('>d', struct.pack('>Q', number))[0]


def unpack(field, string):
    return _struct.unpack(field, string)[0]


import math
import re


def float_to_string(value):
    e = re.search(r'e([-+]?\d+)', str(value))
    if e is None:
        mantissa, exponent = str(value), 0
    else:
        mantissa, exponent = str(value)[:e.start() + 1], int(e.groups()[0])

    mantissa = mantissa.replace('.', '').replace('-', '')
    if mantissa == '': mantissa = '0'
    if exponent >= 0:
        mantissa += '0' * exponent
    else:
        mantissa = mantissa[:exponent] + '.' + mantissa[exponent:]
    return mantissa


