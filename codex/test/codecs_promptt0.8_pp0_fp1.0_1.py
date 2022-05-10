import codecs
# Test codecs.register_error(), should not crash
try:
    codecs.register_error("test.test_crashers", lambda x: (u"", x + 1))
except TypeError:
    pass

import curses
# Test whether the C function _curses.use_env(False) raises an exception.
