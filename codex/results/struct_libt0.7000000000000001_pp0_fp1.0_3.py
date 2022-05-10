import _struct
import _gc
import _warnings
import _weakref
import _sre
import _codecs
import _random
import _bisect
import _heapq
import _lsprof
import _collections

# Import the bootstrap modules, which implement basic services such as
# exception reporting and object space configuration.

import _warnings

# Import the built-in module.  This is a bit of magic, since the built-in
# module is implemented as bytecode.

import __builtin__

# Import the sys module and some of its core routines.  These are
# initialised by new_initconfig().  (Note that new_initconfig() must
# be called before any other function that imports from the sys
# module.)

import sys

# Import the marshal module.  This is a bit of magic, since the
# marshal module is implemented as bytecode.

import marshal

# Import the posix, nt, os2 and mac modules.  These modules are
# special in that they are automatically configured to the specific
# platform, so they are not configured by
