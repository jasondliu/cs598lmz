import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import json
import os
import psutil
import glob
import sys
import argparse
import socket
import subprocess
import shutil
import time
import tarfile
import platform
import uuid
import logging
import logging.handlers
import re
import hashlib
import tempfile
import stat
import urllib2
import yaml
import requests
import traceback
import webbrowser
import ipaddress
import pkg_resources

if sys.version_info >= (3, 0):
    import urllib.parse as urlparse
    from urllib.parse import quote as urlencode
    from urllib.parse import unquote as urldecode
else:
    import urlparse
    from urllib import quote as urlencode
    from urllib import unquote as urldecode

try:
    import pytz
    from pytz import timezone
    from pytz import utc
except Exception as e:
    print(e)
    pass

try:
    from lxml import etree
except:
    print("Failed to import
