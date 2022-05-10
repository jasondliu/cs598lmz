import _struct
import exceptions
import functools
import gettext
import logging
import math
import operator
import os
import re
import socket
import string
import sys
import tempfile
import threading
import traceback
import types
import weakref

from gawkextlib.gwk_exception import GwkException

def _ensure_unicode(s):
    if isinstance(s, unicode):
        return s
    assert isinstance(s, str), repr(s)
    try:
        return s.decode('ascii')
    except UnicodeDecodeError:
        return s.decode('utf8')

def _ensure_utf8(s):
    if isinstance(s, str):
        return s
    assert isinstance(s, unicode), repr(s)
    return s.encode('utf8')

# From http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496735
def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l
