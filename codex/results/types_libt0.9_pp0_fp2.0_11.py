import types
types.ModuleType("PyPDF2")

import logging
try:
    from PyPDF2 import PdfFileWriter, PdfFileReader
except ImportError:
    from pyPdf import PdfFileWriter, PdfFileReader

from PyPDF2.utils import (
    PdfReadError,
    isString,
    isInt,
    ByteStringObject,
    NameObject,
    ArrayObject,
    NumberObject,
    FloatObject,
    IndirectObject,
    NullObject,
    BooleanObject,
    DictionaryObject,
    TextStringObject,
    ContentStream
)
from PyPDF2.compat import unicode

import re, os
from urllib.request import urlopen
import zipfile

from enum import Enum

from tqdm import tqdm

from abc import ABCMeta, abstractmethod, abstractproperty
from itertools import islice
from math import sqrt
from statistics import mean
from copy import copy

from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support

