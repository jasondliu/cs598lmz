import _struct
import _sys
import _thread
import _time
import _traceback
import _types
import _warnings
import _weakref

# Importing _weakref imports _weakrefset, which registers a PEP-451
# __prepare__ implementation that adds an entry to sys.meta_path.  This
# needs to be done before we import any other modules that might use
# __prepare__.

# Importing _weakref also registers a PEP-451 __loader__ for the
# _weakref module.  This needs to be done before we import any other
# modules that might use __loader__.

# Importing _weakref also registers a PEP-451 __spec__ for the
# _weakref module.  This needs to be done before we import any other
# modules that might use __spec__.

# Importing _weakref also registers a PEP-451 __package__ for the
# _weakref module.  This needs to be done before we import any other
# modules that might use __package__.

# Importing _weakref also registers a PEP-451 __path
