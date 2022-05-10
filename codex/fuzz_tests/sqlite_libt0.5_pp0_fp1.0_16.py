import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import argparse
import socket
import ssl
import time

import logging
logging.basicConfig(level=logging.DEBUG)

# https://github.com/fizx/python-ldap3
import ldap3

# https://github.com/jaraco/path.py
from path import path

# https://github.com/alex/python-nmap
import nmap

# https://github.com/mattrobenolt/python-simple-hipchat
import hipchat

# https://github.com/google/google-api-python-client
import googleapiclient.discovery

# https://github.com/google/google-api-python-client
import googleapiclient.errors

# https://github.com/pypa/pip
import pip

# https://github.com/requests/requests
import requests

# https://github.com/kennethreitz/requests-toolbelt
from requests_toolbelt import SSLAdapter

# https://github.com/
