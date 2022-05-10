import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# This is a list of modules that are known to be non-functional.
# We don't want to generate errors for these modules, but we do want
# to generate warnings.

_brokenModules = [
    '_bisect',
    '_codecs',
    '_codecs_cn',
    '_codecs_hk',
    '_codecs_iso2022',
    '_codecs_jp',
    '_codecs_kr',
    '_codecs_tw',
    '_collections',
    '_csv',
    '_ctypes',
    '_elementtree',
    '_functools',
    '_hashlib',
    '_heapq',
    '_hotshot',
    '_json',
    '_locale',
    '_lsprof',
    '_multibytecodec',
    '_multiprocess
