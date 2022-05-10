import lzma
lzma.open

import os
os.path.exists

import pathlib
pathlib.Path

import platform
platform.system

import re
re.compile

import shutil
shutil.rmtree

import socket
socket.gethostbyname

import subprocess
subprocess.run

import sys
sys.platform

import tempfile
tempfile.TemporaryDirectory

import threading
threading.Thread

import time
time.sleep

import urllib.parse
urllib.parse.urlparse

import urllib.request
urllib.request.urlopen

import uuid
uuid.uuid4

import warnings
warnings.warn

import zlib
zlib.decompress

import zipfile
zipfile.ZipFile

import zmq
zmq.Context

import zstd
zstd.ZstdDecompressor

# These are imported by the build system, but not used by the interpreter.
import _collections_abc
import _compat_pickle
import _contextvars
