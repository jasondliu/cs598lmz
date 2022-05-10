import ctypes
import ctypes.util
import threading
import sqlite3
import json
from collections import OrderedDict

from alert import alert
from .iwlibs import struct_iw_range, struct_iw_freq, struct_iwreq, \
    ifreq_set_ex, char_p, iw_freq2float, iw_float2freq, \
    iw_char_to_freq, struct_sockaddr_storage
from .iwks import (
    IW_MAX_TXPOWER, IW_MAX_FREQUENCIES, IW_MAX_BITRATES, IW_MAX_AP,
    IW_AP_MAX, IW_ENCODE_INDEX, SIOCGIWNAME, SIOCGIWNWID,
    SIOCGIWAP, SIOCGIWFREQ, SIOCGIWSENS, SIOCGIWENCODEEXT,
    SIOCSIWFREQ, SIOCSIWNWID, SIOCSIWMODE, SIOCGIWRATE,
    SIOCGIWMODE, SIOCSIWESSID, SIOCSIWNICKN, SIOCGIWNICKN,

