import gc, weakref, operator
from . import _importhook

from . import (datetime, _datetime, _msvccompat, abc, atomic, atexit,
               binascii, bisect, copy, copyreg, csv, doctest, errno,
               grep, functools, gzip, heapq, itertools, http,
               io, json, logging, lzma, math, mmap, multiprocessing,
               os, pdb, pickle, posix, re, shutil, shlex, signal, subprocess,
               sys, tarfile, tempfile, tk, traceback, trace, threading,
               time, token, tokenize, unittest, uuid, warnings,
               weakref, xml, xmlrpc, zipfile, zlib)


try:
    from . import _abc
except ImportError:
    pass


# Do everything under a modern str type
bytes, basestring, unicode = str, str, str

# Pull in stuff
__all__ = (
    'os', 'collections', 'queue', '
