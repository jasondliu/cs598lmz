import _struct
from _struct import *
from _struct import __doc__

from _struct import _clearcache

# This code is used to create the _struct.__doc__ string.

def docformat(fmt, tail):
    """Return a documentation string for the struct format string fmt.

    fmt is the format string, and tail is the trailing part of the
    documentation, e.g. the "See struct.__doc__ for more on format
    strings." string.
    """
    doc = "struct.pack(fmt, v1, v2, ...)\n\n"
    doc += "Return a string containing the values v1, v2, ... packed according\n"
    doc += "to the given format.  See help(%s) for more on format\n" % __name__
    doc += "strings."
    doc += tail
    doc += "\n\n"
    doc += "The variable struct.error is an exception raised on errors."
    doc += "\n\n"
