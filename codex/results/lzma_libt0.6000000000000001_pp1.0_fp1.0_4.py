import lzma
lzma.open = lzma.LZMAFile

import sys
import os
import shutil
import tempfile
import getpass
import subprocess
import sysconfig
import platform
import hashlib
import hmac
import re
import errno
import zipfile
import tarfile
import fnmatch
import stat
import time
import types
import uuid
import xml.etree.ElementTree
import xml.dom.minidom
import xml.parsers.expat
import base64
import datetime
import json
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ElementTree
import xml.etree.ElementTree
import unittest

try:
    import urllib.request as urllib_request
    import urllib.parse as urllib_parse
    import urllib.error as urllib_error
except ImportError:
    import urllib2 as urllib_request
    import urlparse as urllib_parse
    import urllib2 as urllib_error

try:
    import hashlib
