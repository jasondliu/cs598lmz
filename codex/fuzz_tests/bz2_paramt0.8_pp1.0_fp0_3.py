from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = 'bz2'

from io import BytesIO
BytesIO.__module__ = 'io'

from base64 import b64encode, b64decode
b64encode.__module__ = 'base64'
b64decode.__module__ = 'base64'

from datetime import timedelta
timedelta.__module__ = 'datetime'

from re import compile as re_compile, search as re_search
re_compile.__module__ = 're'
re_search.__module__ = 're'

from inspect import isclass as isclass, isfunction as isfunction, ismethod as ismethod
isclass.__module__ = 'inspect'
isfunction.__module__ = 'inspect'
ismethod.__module__ = 'inspect'

from struct import unpack as struct_unpack, calcsize as struct_calcsize
struct_unpack.__module__ = 'struct'
struct_calcsize.__module__ = 'struct'

from sys import stdout as sys_stdout,
