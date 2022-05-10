import lzma
lzma.LZMAError

import zlib
zlib.error

import bz2
bz2.BZ2Error

import zipfile
zipfile.BadZipFile

import tarfile
tarfile.TarError

import sqlite3
sqlite3.Error

import csv
csv.Error

import xml.etree.ElementTree
xml.etree.ElementTree.ParseError

import xml.parsers.expat
xml.parsers.expat.ExpatError

import xml.sax
xml.sax.SAXParseException

import json
json.JSONDecodeError

import ctypes
ctypes.ArgumentError

import ctypes.util
ctypes.util.find_library('c')

import ctypes.wintypes
ctypes.wintypes.error

import ctypes.macholib
ctypes.macholib.dyld.LibraryNotFoundError

import ctypes.macholib.dylib
ctypes.macholib.dylib.dylib_info

import c
