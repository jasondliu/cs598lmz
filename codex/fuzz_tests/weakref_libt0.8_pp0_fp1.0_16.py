import weakref
import gc

from freeorion_tools import try_message_box, console

import freeorion_debug as debug

"""
Provides some functions to check all objects created in/from python for bugs.
See find_leaks_tests.py for examples.
"""

# Two functions for checking for circular references.

def find_circular_references(obj, parent):
    """
    Finds all circular references in obj.
    """
    #print(type(obj), parent, obj)
    if isinstance(obj, weakref.WeakValueDictionary):
        return []
    if isinstance(obj, weakref.ReferenceType):
        return []
    if isinstance(obj, weakref.CallableProxyType):
        return []
    if not isinstance(obj, dict) and not isinstance(obj, list):
        return []
    if not dir(obj):
        return []

    paths = []
    for attr in dir(obj):
        # Skip the dictionary.
        if attr == '__dict__':
            continue
        # Ignore python
