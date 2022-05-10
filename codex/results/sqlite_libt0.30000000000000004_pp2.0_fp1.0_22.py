import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re
import datetime
import subprocess
import json
import requests
import logging
import logging.handlers
import argparse
import traceback
import hashlib
import base64
import binascii
import random
import string
import shutil
import platform
import tempfile
import uuid

# Python 3 compatibility
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

# Python 2.6 compatibility
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

# Python 2.5 compatibility
try:
    from hashlib import sha1
except ImportError:
    import sha
    sha1 = sha.sha

# Python 2.4 compatibility
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

# Python 2.4 compatibility
try:
    from logging import FileHandler
except ImportError:
