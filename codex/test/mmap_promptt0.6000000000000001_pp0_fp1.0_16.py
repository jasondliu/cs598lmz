import mmap
# Test mmap.mmap(0, 1)
# On some platforms, this is a valid call, while on others it will raise
# an error.  If it is valid, then mmap module is good to go.
try:
    mmap.mmap(0, 1)
except Exception:
    mmap = None

import re as _re
import sys as _sys
import time as _time
import datetime as _datetime
import os as _os
import traceback as _traceback
import csv as _csv

from . import file_utils
from . import config
from . import exceptions
from . import string_utils
from . import time_utils
from . import debug_utils
from . import data_utils
from . import xlrd_utils
from . import xlwt_utils
from . import xlsx_utils
from . import openpyxl_utils
from . import pandas_utils
from . import json_utils
from . import csv_utils
from . import sqlite_utils
from . import odbc_utils
from . import ole_utils
from . import oracle_utils
