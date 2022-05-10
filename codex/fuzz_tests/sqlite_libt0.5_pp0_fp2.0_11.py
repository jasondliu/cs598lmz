import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import subprocess
import json
import logging
import base64
import hashlib
import re
import urllib2
import socket
import SocketServer
import select
import ssl
import shutil
import traceback
import random
import string
import datetime
import tempfile
import shutil
import getpass
import platform

from ctypes import *
from ctypes.wintypes import *

import pkg_resources

from Crypto.Cipher import AES
from Crypto import Random


# Global Variables

# The version number of the program
version = "1.0.0"

# The name of the program
name = "Cuckoo Sandbox"

# The name of the author
author = "Cuckoo Sandbox Team"

# The current working directory of the program
cwd = os.getcwd()

# The current user of the program
currentuser = getpass.getuser()

# The current operating system of the program
currentplatform = platform.system()

# The directory of the program
program_directory = os.
