import gc, weakref
from datetime import datetime

from pprint import pformat
from functools import partial

from ._patches import patch_container_put_nowait
from ._utils import time

from ..exceptions import Suspicion
from .._compat import text_type, itervalues, iterkeys
from ..conf import settings

from .backend import PersistentBackend, LruCacheBackend
from .serializers import JsonSerializer
from .types import NonSerializableObject
from .utils import weakmethod

from ..exceptions import ContainerError, InvalidOperationError

from .._compat import text_type, string_types


@six.add_metaclass(ABCMeta)
class AbstractContainer(object):
    '''
    The basic container class
    '''

    max_elements = None
    '''
    Maximum elements allowed in the container
    '''

    serializer = None
    '''
    Serializer object used by the container to convert serializable data to
    and from raw bytes
    '''

    backend = None
    '''
    Backend
