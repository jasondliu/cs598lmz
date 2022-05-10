import gc, weakref
from types import FunctionType
from functools import partial

import six
from six.moves import map, zip

from . import proxy
from .numba_types import is_obj
from .funcdescriptor import generate_ufunc_api_declaration, \
                            generate_registration_code, \
                            CachedUFunc
from .ufunc_db import TypeDatabase

        
class _Parallel(object):
    """
    Allows parallel execution of *func* on *type_db* database entries.
    The function *func* is called with keyword arguments *kwargs* and
    will be executed on each type database entry. It should return
    a Numba type as a result.
    
    The call to func on a type database entry looks like this:
    
    func(**kwargs, entry=entry, type_db=type_db)
    
    """
    def __init__(self, func, type_db, kwargs=None):
        self.func = func
        self.type_db = type_db
        self.kwargs
