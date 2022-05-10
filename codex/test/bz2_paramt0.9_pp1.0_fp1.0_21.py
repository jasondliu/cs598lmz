from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor
import calendar
from datetime import datetime, timedelta
from email import utils
import gzip
import html
from io import BytesIO
from itertools import chain
import math
from typing import BinaryIO, Dict, Generator, List, Optional, Sequence, Tuple, Union
from urllib.parse import quote
import urllib.error, urllib.request
import xml.dom.minidom
import xml.etree.ElementTree as ET
from xml.etree.cElementTree import fromstring, fromstringlist
from xml.parsers.expat import ExpatError


__all__ = ['open', 'parse', 'parse_xml', 'parse_xmlbz2']
_LZMA_SUPPORTED = False
try:
    import lzma
    _LZMA_SUPPORTED = True
except ImportError as e:
    if "not built yet" not in str(e):
        raise

