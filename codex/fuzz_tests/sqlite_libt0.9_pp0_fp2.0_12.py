import ctypes
import ctypes.util
import threading
import sqlite3
import os
from ConfigParser import ConfigParser
from hashlib import sha256
from sflock import File
from sflock.abstract import FileList, FileObject, UnsupportedTypeException
from sflock.abstract import Extractor
from sflock.pick import extract
from sflock.pick import unpack
from sflock.pick import detect_type
from common.CCD import librt
from common.CCD import CCD_DATABASE
import struct, ctypes

#from scan import common
import httplib
import json

class libbfd_log_file(Extractor):
    name = "libbfd_log_file"
    version = "20160623"
    tool = "no tools version number"
    mime = ['application/x-sharedlib', 'application/x-archive', 'application/x-dynamiclib', 'application/x-executable', ]
    author = "mingyi.gu@trendmicro.com"
    dblocation = os.path.dirname(CCD_DATABASE)

    def _
