import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import zipfile
import argparse

try:
    import win32com.client
except (ImportError, ModuleNotFoundError):
    pass

try:
    import xlrd
except (ImportError, ModuleNotFoundError):
    pass


# win32com.client.constants : https://msdn.microsoft.com/ja-jp/library/office/jj692818.aspx
xl_constants = {
    'xlContinuous': 1,
    'xlEdgeBottom': 9,
    'xlEdgeLeft': 7,
    'xlEdgeRight': 10,
    'xlEdgeTop': 8,
    'xlInsideHorizontal': 12,
    'xlInsideVertical': 11,
    'xlThin': 2,
    'xlUpward': 0,
    'xlDownward': 1,
    'xlTickMarkOutside': 2,
    'xlTickLabelPositionNone': -4142
