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
