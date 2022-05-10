import ctypes
ctypes.cast(0, ctypes.py_object).value = 0
'''

# Back to the normal imports
import re
import os
import sys
import pprint
import socket
import tempfile
import time
import datetime
import getpass
import json
import yaml
import hashlib
import logging
import argparse
import collections
import threading
import traceback
import subprocess
import contextlib

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
try:
    import urllib.error
except ImportError:
    import urllib2 as urllib_error
try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

try:
    import http.client as httplib
except ImportError:
    import httplib
try:
    import http.client as http_client
except ImportError:
    import httplib as http_client

try:
    import
