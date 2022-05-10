import mmap
import os
import subprocess
import sys
import socket
import re
import psutil
import shutil
import getpass
import datetime
import platform

try:
    import pytest
except ImportError:
    print("Warning: Some tests require pytest")
    pytest = None

try:
    import requests
except ImportError:
    print("Warning: Some tests require requests")
    requests = None

try:
    import snappy
except ImportError:
    print("Warning: Some tests require python-snappy")
    snappy = None

try:
    import lz4.block
except ImportError:
    print("Warning: Some tests require python-lz4")
    lz4 = None

try:
    import cchardet
except ImportError:
    print("Warning: Some tests require chardet")
    cchardet = None

try:
    import pylint
except ImportError:
    print("Warning: Some tests require pylint")
    pylint = None

try:
    import click
except ImportError:
    print
