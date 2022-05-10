import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

import sys, os

if sys.version_info[0] == 2:
    os.environ['HOME'] = '/home/languitar'

import os
os.environ['LANGUAGE'] = 'en_US.UTF-8'
os.environ['LANG'] = 'en_US.UTF-8'
os.environ['LC_ALL'] = 'en_US.UTF-8'
os.environ['LC_CTYPE'] = 'en_US.UTF-8'

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

import codecs
import json
import gzip
import base64
import hashlib

from datetime import datetime
from urllib.parse import urlparse
from collections import OrderedDict

from anki.utils import ids2str, intTime, splitFields
from anki.template import TemplateRenderContext, render_to_unicode
from anki.hooks import runFilter
