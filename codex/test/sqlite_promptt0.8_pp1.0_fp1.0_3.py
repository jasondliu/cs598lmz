import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import os.path
import os
import re
import sys
import subprocess
import time
import urllib
import shutil
import random
import glob
import string
import logging
import uuid
import codecs
import tempfile
import hashlib

log = logging.getLogger(__name__)

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    # try to import easy_install before setuptools
    import pkg_resources
    import setuptools
    # we want setuptools' namespace, but not its monkeypatches
    # so we import setuptools *after* we've imported pkg_resources
    import pkg_resources
    import setuptools
    setuptools.bootstrap_install_from = None
except ImportError:
    ez = {}
    # easy_install might be missing too
    # if it is, the message will read something like:
    # No module named 'pkg_resources'
    # PYTHONPATH = ['/usr/lib/python3.6/dist
