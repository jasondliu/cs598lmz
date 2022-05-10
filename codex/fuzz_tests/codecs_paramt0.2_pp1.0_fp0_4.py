import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The following is a hack to make sure that the correct version of
# pywin32 is imported.  See http://bugs.python.org/issue5853 for
# details.
import sys
if sys.version_info[:2] == (2, 6):
    import _winreg as winreg
else:
    import winreg

import win32api
import win32con
import win32gui
import win32process
import win32security
import win32ts
import win32ui
import win32ui_server
import win32wnet

import pywintypes

# The following is a hack to make sure that the correct version of
# pywin32 is imported.  See http://bugs.python.org/issue5853 for
# details.
import sys
if sys.version_info[:2] == (2, 6):
    import _winreg as winreg
else:
    import winreg

import win32api
import win32con
import win32gui
import win32process
import win32security
import win32ts
