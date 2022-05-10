import weakref
import sys
import os

from . import _sre
from . import sre_constants
from . import sre_parse

__all__ = [
    "compile", "isstring", "match", "purge", "search", "split", "findall",
    "finditer", "sub", "subn", "escape", "I", "IGNORECASE", "L", "LOCALE", "M",
    "MULTILINE", "S", "DOTALL", "X", "VERBOSE", "error",
]

MAXREPEAT = 65535

# public symbols
I = IGNORECASE = sre_constants.SRE_FLAG_IGNORECASE # ignore case
L = LOCALE = sre_constants.SRE_FLAG_LOCALE # assume current 8-bit locale
U = UNICODE = sre_constants.SRE_FLAG_UNICODE # assume unicode locale
M = MULTILINE = sre_constants.SRE_FLAG_MULTILINE # make anchors look for newline
S = DOT
