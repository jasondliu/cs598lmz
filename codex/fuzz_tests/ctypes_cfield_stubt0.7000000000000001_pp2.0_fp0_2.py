import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__repr__ = lambda self: '{0}.{1}'.format(self._ctype_, self.name)
ctypes.CField.__str__ = lambda self: '{0}.{1}'.format(self._ctype_, self.name)
ctypes.CField.__format__ = lambda self, format_spec: '{0} {1}'.format(
    format(self._ctype_, format_spec), self.name)

#
# Now, the remaining non-ctypes code:
#

import sys
import traceback

#
# Syntax highlighters
#

class PygmentsSyntaxHighlighter:
    def __init__(self, language):
        self.language = language
        self.formatter = pygments.formatters.Terminal256Formatter()

    def highlight(self, s):
        return pygments.highlight(s, pygments.lexers.get_lexer_by_name(self.language), self.formatter)

class PlainTextSyntaxHighlighter:
