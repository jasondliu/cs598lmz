import ctypes
ctypes.cast(id(0), ctypes.py_object).value

# The above is equivalent to:

import sys
sys.getrefcount(0)

# The above is equivalent to:

import weakref
len(weakref.getweakrefs(0))

# The above is equivalent to:

import gc
gc.get_referents(0)

# The above is equivalent to:

import gc
gc.get_referrers(0)

# The above is equivalent to:

import gc
gc.get_objects()

# The above is equivalent to:

import gc
gc.get_stats()

# The above is equivalent to:

import gc
gc.get_threshold()

# The above is equivalent to:

import gc
gc.set_debug(gc.DEBUG_STATS)

# The above is equivalent to:

import gc
gc.set_debug(gc.DEBUG_LEAK)

# The above is equivalent to:

import gc
gc.set_debug(gc.DEBUG
