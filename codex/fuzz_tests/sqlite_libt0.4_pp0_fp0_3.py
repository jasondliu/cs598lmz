import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import json
import traceback
import logging
import logging.handlers
import re
import argparse
import subprocess
import socket
import struct
import fcntl
import textwrap
import platform

# The following is for python 2.7 support
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# The following is for python 3.x support
try:
    import queue
except ImportError:
    import Queue as queue

# The following is for python 2.7 support
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

# The following is for python 3.x support
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# The following is for python 2.7 support
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

# The following is for python 2.7 support
try:
   
