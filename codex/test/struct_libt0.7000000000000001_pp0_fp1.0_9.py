import _struct
import pickle
import traceback
import xmlrpclib
import logging
from xmlrpclib import Binary, Fault
from threading import Lock
from .. import mgr
from .. import logger
from ..security import Scope
from .. import orchestrator
from mgr_module import MgrModule, HandleCommandResult
from ..controllers.rbd import RbdController

try:
    import rados
except ImportError:
    rados = None

try:
    from typing import Dict, Any, Optional, List, TypeVar, Type, cast, Callable
except ImportError:
    pass

try:
    # typing in python 3.5.2 has generic_new
    from typing import GenericMeta
except ImportError:
    # generic_new added in python 3.6.1
    class GenericMeta(type):
        pass


T = TypeVar('T')


class _CephModule(MgrModule, GenericMeta):
    def __init__(self, *args, **kwargs):
        super(_CephModule, self).__init__(*args, **kwargs)
