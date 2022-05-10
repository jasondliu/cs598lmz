import _struct
import _time
import _thread
import _warnings
import _weakref

# Modules that should be loaded as builtins
_BUILTIN_MODULES = [
    '_ast', '_bisect', '_codecs', '_collections', '_datetime', '_functools',
    '_hashlib', '_heapq', '_io', '_locale', '_md5', '_operator', '_pickle',
    '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha512', '_signal',
    '_sre', '_stat', '_string', '_struct', '_symtable', '_thread', '_tracemalloc',
    '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'cmath', 'errno',
    'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt',
    'nt', 'parser',
