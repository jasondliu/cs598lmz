import ctypes
import ctypes.util
import threading
import sqlite3
import os
import struct
import pprint
import base64
import json
import re
import urllib
import math
import locale
import string
import sys
import textwrap
import traceback
import binascii

VERBOSE = False

# http://odfpy.forge.osor.eu/
# http://www.odfpy.org/
from odf.opendocument import load
from odf.opendocument import OpenDocumentPresentation
from odf.draw import Image
from odf.opendocument import OpenDocumentText
from odf.opendocument import OpenDocumentSpreadsheet
from odf.text import H, P
from odf.style import Style, TextProperties, ParagraphProperties, TableCellProperties
from odf.table import Table, TableRow, TableColumn, TableCell, CoveredTableCell
from odf.draw import Frame, TextBox
from odf.element import Element
from odf.office import DocumentContent
from odf  import teletype
from odf.number import NumberCurrencyStyle
from odf.number import NumberStyle, NumberC
