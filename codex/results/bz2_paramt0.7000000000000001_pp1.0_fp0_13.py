from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = lambda self, x: x
import re, sys, os, os.path, zlib
from cStringIO import StringIO

import logging
log = logging.getLogger('gendeps')

# Maps from filename to contents
files = {}

# Maps from filename to dependencies
deps = {}

# Maps from filename to cache keys
cacheKeys = {}

# Regex for detecting what files are included.
includeRegex = re.compile(r'^\s*#include\s*"([^"]+)"')

# Regex for detecting which files are framework dependencies
frameworkRegex = re.compile(r'^\s*#import\s*<([^>]+)>')

# Regex for detecting which files are system dependencies
systemRegex = re.compile(r'^\s*#import\s*<([^>]+)>')

# Regex for detecting which files are local dependencies
localRegex = re.compile(r'^\s*#import\s*"([^"]+)"')

# Regex for detecting
