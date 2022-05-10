import ctypes
import ctypes.util
import threading
import sqlite3
import json
import time
import os
import sys
import errno
import struct
import re
import shutil
import logging
import logging.handlers
import datetime
import urllib2
import logging.config
from Crypto.PublicKey import RSA
from Crypto.Random import random
from Crypto.Hash import SHA
from Crypto.Cipher import AES

# TODO:
# - check if the directory exists before calling os.mkdir
# - add a check that the directory is writable
# - add a check that the directory is owned by the user
# - check if the file exists before calling os.mknod
# - add a check that the file is writable
# - add a check that the file is owned by the user
# - add a check that the file is a socket
# - add a check that the socket is writable
# - add a check that the socket is owned by the user
# - check if the file exists before calling os.unlink
# - add a check that the file is owned by the user
# - add a check that the file is a socket
# - check if the directory exists before calling
