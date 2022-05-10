import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import logging
import logging.handlers
import signal
import socket
import fcntl
import struct
import errno
import traceback
import subprocess
import re
import string
import random
import shutil
import json
import hashlib
import urllib
import urllib2
import httplib
import base64
import tempfile
import glob
import copy
import stat
import email.utils
import datetime
import platform
import zipfile
import tarfile
import getpass
import pwd
import grp
import locale
import gettext
import xml.etree.ElementTree as ET

from ConfigParser import ConfigParser
from optparse import OptionParser
from subprocess import Popen, PIPE
from collections import defaultdict
from collections import namedtuple
from distutils.version import LooseVersion

#
# Global variables
#

# The version of this program
VERSION = "0.9.2"

# The version of the configuration file
CONFIG_VERSION = "0.9.2"

# The version of the database

