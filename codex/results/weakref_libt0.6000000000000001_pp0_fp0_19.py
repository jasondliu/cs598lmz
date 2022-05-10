import weakref
import pickle
import sys
import os

__all__ = ['get_shared_objects']

_shared_objects = {}

def get_shared_objects():
    """
    Returns a map of all shared objects.
    """
    return _shared_objects

def get_shared_object(name, default = None):
    """
    Returns the shared object with the given name or default if the
    object does not exist.
    """
    return _shared_objects.get(name, default)

def set_shared_object(name, obj):
    """
    Set the shared object with the given name to the given object.
    """
    _shared_objects[name] = obj

def get_shared_object_path(name, create = False):
    """
    Returns the path to the file containing the given shared object.
    """
    shared_object_path = os.path.join(get_shared_objects_path(), name)
    if create and not os.path.exists(shared_object_path):
        os.makedirs(shared_object
