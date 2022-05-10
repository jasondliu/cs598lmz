import codecs
# Test codecs.register_error()
import datetime
import glob
import gzip
import inspect
import io
import json
import math
import os
import pprint
import random
import re
import shutil
import string
import sys
import tempfile
import time
import traceback
import unittest
import warnings
import xml.etree.ElementTree as ET

from distutils.version import LooseVersion

# Test the C version of the ElementTree module
try:
    import xml.etree.cElementTree as cET
except ImportError:
    cET = None

# Test the _elementtree module
try:
    import _elementtree
except ImportError:
    _elementtree = None

# Test the pyexpat module
try:
    import pyexpat
except ImportError:
    pyexpat = None

try:
    import bz2
except ImportError:
    bz2 = None

try:
    import lzma
except ImportError:
    lzma = None

try:
    import zlib
except ImportError:
    zlib = None

try
