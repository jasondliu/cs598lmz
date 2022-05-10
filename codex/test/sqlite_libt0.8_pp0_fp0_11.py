import ctypes
import ctypes.util
import threading
import sqlite3

import gc

g_debug = True

# user32 library
###############################################################################
user32 = ctypes.windll.user32

# constants
WM_SHOWWINDOW           = 0x00000018
WM_SIZE                 = 0x0000005
WM_QUIT                 = 0x00000012
WM_DESTROY              = 0x00000002
WM_CLOSE                = 0x10
WM_SETCURSOR            = 0x20
WM_SETTEXT              = 0x000C
WM_GETTEXT              = 0x000D
WM_GETTEXTLENGTH        = 0x000E
WM_COMMAND              = 0x0111
WM_NOTIFY               = 0x004E
WM_PARENTNOTIFY         = 0x0210
WM_LBUTTONDOWN          = 0x0201
WM_LBUTTONUP            = 0x0202
WM_LBUTTONDBLCLK        = 0x203
WM_RBUTTONDOWN          = 0x204
WM_RBUTTONDBLCLK        = 0x206
WM_RBUTTON
