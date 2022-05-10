import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import datetime
import os
import sys
import time

import win32com.client
import xlwings as xw

import pandas as pd
import numpy as np

from . import util
from . import xlutil
from . import xlreport
from . import xlform
from . import xlrun
from . import xlfile
from . import xlconfig
from . import xlcons
from . import xlwbook
from . import xlwsheet
from . import xlwrange
from . import xlwchart
from . import xlwpicture
from . import xlwshape
from . import xlwshape_chart
from . import xlwshape_picture
from . import xlwshape_textbox
from . import xlwshape_table
from . import xlwshape_group
from . import xlwshape_comment
from . import xlwshape_sparkline
from . import xlwshape
