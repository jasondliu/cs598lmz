import lzma
# Test LZMADecompressor
#from lzma import *
#from lzma import check
from bz2 import BZ2Decompressor
from gzip import GzipFile, GzipFileError
from subprocess import Popen, PIPE


#from cStringIO import StringIO
import os
from os.path import join
import sys
from sys import stdout
import time
from time import sleep
from time import time
#from urllib import urlopen
from urllib2 import urlopen
from urlparse import urlparse
from urlparse import urljoin
import xml.sax
from xml.sax.handler import ContentHandler
from xml.sax import parse
from zipfile import BadZipfile
from zipfile import ZipFile
from zipfile import ZipInfo
#from zipfile import bz2
from zipfile import is_zipfile
from zipfile import ntpath
from zipfile import struct
from zipfile import utf8
import zlib

from logger import log
#from logger import log_exc
from mbtools import progress_bar
from mbtools import remove_prefix_if_present
from m
