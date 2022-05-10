import gc, weakref
from . import _thread
from . import _threading_local

# Maps types to a list of weak references to objects of that type.
# This essentially maps the id(object) to a list of weak references.
# This is used to track all objects that have a finalizer.
_objects = {}

# Maps ids to finalizer functions.
_finalizer_registry = {}

# Maps ids to a weakref to an object.
# This is used to track all objects that have a finalizer.
_finalizer_cache = {}

# Lock used to protect the registries.
_registry_lock = _thread.allocate_lock()

# Lock used to protect the creation of new weakrefs.
_weakref_lock = _thread.allocate_lock()

# This lock is used to protect the creation of new weakrefs when the
# GIL is released.  It must be a reentrant lock so that a thread can
# release the GIL, create a weakref, and reacquire the GIL without
# deadlocking.
_py3k_weakref_
