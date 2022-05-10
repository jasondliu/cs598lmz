import gc, weakref
from collections import OrderedDict
from tabulate import tabulate
import numpy as np

# Keep track of objects that are alive
_alive_objects = OrderedDict()
_id_generator = itertools.count(start=0)

class Scoreboard(object):
    """
    This class is intended to keep a handle on all known objects.
    
    It should be a single global instance.
    """
    def __init__(self):
        self._objects = weakref.WeakValueDictionary()
        
    def add_object(self, obj):
        """
        Add an object to be tracked.
        
        Once added, it will stay in the list until it is garbage collected.
        """
        self._objects[id(obj)] = obj
        
    def get_objects(self, alive=True):
        """
        Return a list of objects.
        
        By default, all the objects in the list are alive, but you can get the dead objects
        by setting the `alive` argument to `False`.
        """
        if alive:

