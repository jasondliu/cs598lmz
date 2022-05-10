import codecs
# Test codecs.register_error(), should not crash
try:
    codecs.register_error("test.test_crashers", lambda x: (u"", x + 1))
except TypeError:
    pass

import curses
# Test whether the C function _curses.use_env(False) raises an exception.
try:
    curses._curses.use_env(False)
except TypeError:
    pass

import gc
gc.collect()
# Test whether gc.garbage is writable, should not crash
gc.garbage.append(gc.garbage)

import grp
# Test whether grp.getgrall() raises an exception, should not crash
try:
    grp.getgrall()
except TypeError:
    pass

import httplib
# Test whether httplib raises exceptions, should not crash
try:
    httplib.HTTPException
except TypeError:
    pass

# Test whether the C function _json.encode_basestring raises an exception,
# should not crash
import _json
try:
    _json.encode_basest
