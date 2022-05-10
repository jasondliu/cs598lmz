import codecs
# Test codecs.register_error('test', codecs.ignore_errors)

import os
import os.path
import copy

import logging
from logging import info, warning, error
from logging import debug as debug_log

import json

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import re

from traceback import print_exc

import threading

