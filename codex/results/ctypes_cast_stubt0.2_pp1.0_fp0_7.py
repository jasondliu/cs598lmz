import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in Python 2.7.3
# See http://bugs.python.org/issue15881#msg170215
try:
    import thread
except ImportError:
    import _thread as thread

import time

import sys
import os
import re
import subprocess
import signal
import traceback
import logging
import logging.handlers
import json
import argparse
import socket
import struct
import random
import string
import base64
import hashlib
import hmac
import binascii
import errno
import ssl
import select
import threading
import Queue
import collections
import datetime
import platform
import copy
import tempfile
import shutil
import glob
import ctypes
import ctypes.util
import imp
import getpass
import pwd
import grp
import locale
import codecs
import stat
import fnmatch
import xml.dom.minidom
import xml.etree.ElementTree
import xml.parsers.expat
import xml.sax.s
