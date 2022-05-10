import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import subprocess
import re
import glob
import shutil
import tempfile
import logging
import json
import gzip
import tarfile
import zipfile
import urllib
import urllib2
import base64
import hashlib
import getpass
import platform
import argparse
import ConfigParser
import threading
import Queue
import webbrowser

try:
    import xml.etree.ElementTree as ET
except ImportError:
    import elementtree.ElementTree as ET

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    import cjson as json
except ImportError:
    import json

try:
    from Crypto.Cipher import AES
except ImportError:
    AES = None

try:
    import keyring
except ImportError:
    keyring = None

try:
