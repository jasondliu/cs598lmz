import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import re
import time
import subprocess
import threading
import traceback
import socket
import json
import urllib
import urllib2
import urlparse
import base64
import hashlib
import hmac
import mimetypes
import tempfile
import shutil
import Queue
import optparse

try:
    import simplejson
except ImportError:
    simplejson = None

try:
    import pynotify
except ImportError:
    pynotify = None

try:
    import gtk
except ImportError:
    gtk = None

try:
    import appindicator
except ImportError:
    appindicator = None

try:
    import keyring
except ImportError:
    keyring = None

