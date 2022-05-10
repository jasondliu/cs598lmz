import gc, weakref
from weakref import WeakKeyDictionary

from .entity import *
from .component import *
from .system import *
from .exceptions import *

from . import systems

class World(object):
    """
    The central class of the ECS.
    This class manages all entities and systems.
    """
    
    def __init__(self):
        self._entities = []
        self._components = {}
        self._systems = []
        
        self._systems_by_class = {}
        self._entities_by_component = {}
        
        self._entities_by_id = {}
        
        self._entity_id_counter = 0
        
        self._running = False
    
    # ==============================================================
    # ENTITIES
    # ==============================================================
    
    def create_entity(self, *components):
        """
        Create a new entity with the given component classes.
        """
        new_entity = Entity(self, self._entity_id_counter)
        self._entity_id_counter += 1

