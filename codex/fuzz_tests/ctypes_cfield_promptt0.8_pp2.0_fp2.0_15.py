import ctypes
# Test ctypes.CField
import datetime

os.environ["PATH"] += ";."

# for unit tests
import logging
# logging.basicConfig(level=logging.DEBUG)

import os
import subprocess

import pyads
import pyads.util
import pyads.definitions
import pyams

# TODO: fix the following code
# # pylint: disable=C0103
# # pylint: disable=W0613
# # pylint: disable=W0622
# # pylint: disable=W0212

# # pylint: disable=C0111


def getAdsLibPath():
    if os.name == 'nt':
        ads_lib_path = 'lib\\adsapi.dll'
    elif os.name == 'posix' and os.uname()[0] == 'Linux':
        ads_lib_path = 'lib/libadsapi.so'
    else:
        raise Exception('Operating system not supported!')
    return ads_lib_path


def getAmsLibPath():
    if os.
