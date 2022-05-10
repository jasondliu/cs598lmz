import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import os
import io
import sys
import struct
import binascii
import subprocess
import re
import sys
#from Tkinter import *
import time
import datetime
import smtplib
import requests
import shutil
import base64
import datetime
import os.path
import traceback
import random
import logging
import email
import email.mime.application
import email.mime.multipart
import email.mime.text
import email.mime.base
import multiprocessing
import base64
import ConfigParser
import ast

from lib import *
from daemon import Daemon
from webservice import WebService

#####################################################################################
# SQLITE_DEFAULT_FOREIGN_KEYS is defined only in sqlite3.h of Python 3.3.2 and later.
# To enable foreign keys in sqlite3 of Python 2.7, it is necessary to define the
# constant here.
#####################################################################################
try:
    sqlite3.SQLITE_DEFAULT_FOREIGN_KEYS
except:
    sqlite3.
