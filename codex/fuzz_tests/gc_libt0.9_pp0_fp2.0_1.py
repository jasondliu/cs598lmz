import gc, weakref
import numpy as np
import os.path
import struct as st

def alias_libname(libname, version=None):
    if libname.startswith(('-l', 'lib')):
        name = libname[2:]
    else:
        name = os.path.split(libname)[1]
        if not name or name == libname:
            return libname, None
    postfix = ''
    if name.startswith('librt'):
        name = 'librt'
        postfix = 'rt'
    elif name.endswith('.rt'):
        postfix = 'rt'
        name = name[:-3]
    elif name.startswith('lib'):
        postfix = name[3:]
    elif name.endswith('.so'):
        postfix = name[:-3]
    elif name.endswith('.a'):
        return libname, None
    name = '_lib' + name.replace('.', '_').replace('-', '_').
