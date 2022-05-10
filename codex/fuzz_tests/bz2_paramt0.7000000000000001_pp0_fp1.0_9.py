from bz2 import BZ2Decompressor
BZ2Decompressor.__init__ = lambda s, file_obj=None: None
from cPickle import dumps, load, loads, UnpicklingError
from cStringIO import StringIO
from csv import DictWriter, DictReader
from functools import wraps
from glob import glob
import gzip
from itertools import izip, repeat
from math import log
from os import environ, fdopen, getcwd, listdir, makedirs, remove
from os.path import basename, dirname, exists, expanduser, getsize, isdir, join
from re import compile as re_compile, findall, match
from shutil import copy as copyfile, copytree, rmtree
import signal
from tarfile import open as taropen
from tempfile import mkdtemp, mkstemp
from time import sleep
from urllib import urlretrieve
from zipfile import ZipFile

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from settings import settings

#TODO: add to settings:
#     'MEM
