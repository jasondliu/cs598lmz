import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.py_object)

# Functions that are wrapped by the glk function object
# This is just to avoid having to do if id in map.__glk

glk_functions = ('glk_exit','glk_set_interrupt_handler',
         'glk_tick','glk_gestalt','glk_gestalt_ext','glk_char_to_lower',
         'glk_char_to_upper')

def map_function(function, ret_type = None, event = False, inspect = None):
    """Adds mapping for the function

    function -- The name of the function in the Glk library
    ret_type -- The return type of the function, None for Py_None
    event -- Does the function expect a winid_t?
    inspect -- Specifies the args that are pointers

    """
    def wrapper(self, *args):
        """Wraps the Glk function. Returns Py_None if ret_type is None"""
        if event:
            args = (self.events.events[self.events
