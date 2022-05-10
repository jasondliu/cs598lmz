import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import datetime
import random
import string
import logging
import logging.handlers
import json
import re
import urllib2
import requests
import httplib
import urllib
import urllib2
import urlparse
import cookielib
import socket
import socks
import mechanize
import threading
import Queue
import gzip
import zlib
import ssl
import base64
import hashlib
import binascii
import argparse
import getpass
import readline
import subprocess
import platform
import fcntl
import termios
import struct
import signal

from optparse import OptionParser
from bs4 import BeautifulSoup
from subprocess import Popen, PIPE
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
from requests.packages.urllib3.exceptions import SNIM
