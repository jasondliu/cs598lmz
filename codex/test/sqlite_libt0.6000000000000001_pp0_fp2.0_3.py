import ctypes
import ctypes.util
import threading
import sqlite3
import zlib
import json
import time
import sys
import os
import re
import io
import fcntl
import errno
import binascii
import traceback
import socket
import struct
import ssl
import tempfile
import select
import signal
import hashlib
import random
import hmac
import base64
import subprocess
import collections

##
# Stuff that should be in Python's standard library
##

def urlsafe_b64encode(s):
    return base64.urlsafe_b64encode(s).replace(b'=', b'')

def urlsafe_b64decode(s):
    padding_needed = len(s) % 4
    if padding_needed:
        s += b'=' * (4 - padding_needed)
    return base64.urlsafe_b64decode(s)

