import types
types.FunctionType = types.BuiltinFunctionType

import inspect
import os
import sys
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast
import astor
import hashlib

sys.path.append('../..')
import rnn
import rnn.ast_processing as processing
import rnn.util as util

def get_fpaths(chunk_size=0):
    fpaths = []
    fnames = [i.strip() for i in os.popen("find ./ | egrep \".py$\"").readlines()]
    chunks = util.make_chunks(fnames, chunk_size)
    for fnames in chunks:
        fpaths += [os.path.abspath(i) for i in fnames]
    return fpaths

def get_fpaths_by_sfile(fpath):
    sfile = processing.get_sfile_obj(fpath)
