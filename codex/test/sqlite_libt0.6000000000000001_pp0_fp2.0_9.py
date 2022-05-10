import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import sys
import os
import re
import socket
import random
import traceback
import trace
import getopt
import time
import urllib2
import hashlib
import subprocess
import platform
import cPickle as pickle
import zlib
import string
import math
import glob
import shutil
import tempfile
import zipfile
import Queue
import simplejson as json
import ConfigParser

from ctypes import *
from struct import *

try:
    import pygeoip
    geoip_loaded = True
except:
    geoip_loaded = False

#
# TODO:
#
#
#


# globals

# if set to True, will cause process to exit after processing current work
# if set to False, will cause process to wait for more work
# this is used to gracefully exit the process
shutdown = False

# if set to True, will cause process to exit after processing current work
# if set to False, will cause process to wait for more work
# this is used to gracefully exit the process
restart
