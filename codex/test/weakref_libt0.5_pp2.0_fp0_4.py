import weakref

from . import config
from . import event
from . import event_type
from . import event_handler
from . import event_manager
from . import util
from . import world
from . import world_object

class ObjectManager(object):
    """
    The ObjectManager handles the creation, destruction and lookup of objects.
    """
    def __init__(self, world):
        self._world = weakref.proxy(world)
        self._objects = {}
        self._object_ids = {}
        self._object_names = {}
        self._object_types = {}
        self._object_type_ids = {}
        self._object_type_names = {}
        self._object_type_counts = {}
        self._object_type_event_handlers = {}
        self._object_event_handlers = {}
        self._object_event_handler_ids = {}

