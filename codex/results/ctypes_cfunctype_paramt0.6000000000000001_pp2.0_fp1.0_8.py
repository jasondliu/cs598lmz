import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

def func(data):
    print("func data:", data)
    return 1

def callback(data, userdata):
    print("callback data:", data, "userdata:", userdata)
    return 1

cfunc = FUNTYPE(func)
ccallback = FUNTYPE(callback)

#
#
#

import numpy as np
from numpy.ctypeslib import ndpointer

#
#
#

#
#
#

if __name__ == "__main__":

    import os
    import sys
    import json

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input json file", type=str)
    parser.add_argument("-o", "--output", help="output json file", type=str)
    parser.add_argument("-s", "--start", help="start index", type=int)
    parser.add_argument("-e", "--
