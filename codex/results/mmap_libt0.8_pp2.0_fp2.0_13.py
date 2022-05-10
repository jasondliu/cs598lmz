import mmap
import os.path
import re
import string
import sys
import urllib

# Version number
VERSION = '0.6'

# Usual defaults
DEFAULT_LIB_DIR = "/lib"
DEFAULT_LIB64_DIR = "/lib64"
DEFAULT_PAGE_SIZE = 4*1024
DEFAULT_MIN_ALLOC_SIZE = 4*1024
DEFAULT_REPEATS = 1
DEFAULT_SILENT = False
DEFAULT_QUIET = False
DEFAULT_ALL = False
DEFAULT_SHOW_MEMINFO = False
DEFAULT_SHOW_HEAPINFO = False
DEFAULT_SHOW_STACKINFO = False
DEFAULT_SHOW_LECTUREINFO = False
DEFAULT_BUILDID_DIR = "build-id"

# Magic signatures
ELF_SIGNATURE = "\x7f" + "ELF"
ELF_CLASSES = (
  ("32-bit", "\x01"),
  ("64-bit", "\x02")
)
ELF_DATA_ENCODINGS = (
  ("little endian", "\x01
