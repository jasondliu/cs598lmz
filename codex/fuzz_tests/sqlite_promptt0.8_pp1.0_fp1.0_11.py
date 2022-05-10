import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
from time import sleep, time
from sys import exit

from constants import V4L2_CAP_VIDEO_CAPTURE, V4L2_PIX_FMT_YUYV, V4L2_MEMORY_MMAP
from constants import V4L2_CAP_STREAMING, V4L2_CID_EXPOSURE
from constants import V4L2_CID_GAIN, V4L2_CID_WHITE_BALANCE_TEMPERATURE
from constants import V4L2_CID_DO_WHITE_BALANCE
from constants import V4L2_CID_HFLIP, V4L2_CID_VFLIP
from constants import V4L2_CID_ZOOM_ABSOLUTE, V4L2_CID_FOCUS_ABSOLUTE
from constants import V4L2_CID_FOCUS_AUTO, V4L2_CID_FOCUS_RELATIVE
from constants import V4L2_CID_AUTO_FOCUS_START
