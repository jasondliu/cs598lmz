import ctypes
ctypes.cast(0, ctypes.py_object).value = 3

import os
import sys
import time
import platform
import socket
import argparse
import json
import requests
import logging
import logging.handlers
from datetime import datetime
from threading import Thread
from threading import Event
from pkg_resources import parse_version
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import SubjectAltNameWarning

