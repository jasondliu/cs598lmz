import gc, weakref
from weakref import WeakKeyDictionary
from types import MethodType
from functools import wraps
from collections import defaultdict
from . import util
from . import events
from . import exceptions
from . import interfaces
from . import logging
from . import attributes

log = logging.getLogger(__name__)

class HasProps(object):
    """ Base class for all plot objects that have properties on them.

    Generally, users won't need to use this class directly.

    """

    # A class attribute to generate sequential, unique, session IDs.
    _session_id_seq = 0

    # Maps session ID to a weak reference to the object.
    _instances = WeakKeyDictionary()

    # Maps session ID to a weak reference to the object.
    _instances_by_name = WeakKeyDictionary()

    # Maps session ID to a weak reference to the object.
    _instances_by_name_and_group = WeakKeyDictionary()

    # Maps session ID to a weak reference to the object.
    _instances_by_name_and_subgroup = Weak
