import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def func_factory(func):
    """Function factory so that we use None for the defaults."""
    return lambda *args, **kwargs: func(*[None if arg is None else arg for arg in args], **kwargs)

PYFUNTYPE = FUNTYPE(func_factory)

def make_vk_object(type_name_or_func, init_func, additional_params=None, type_name_is_func=False, additional_static_methods=None):
    """
    Create a new class which wraps a vulkan object.
    type_name_or_func is either a string name of the value we expect to return from vkGetInstanceProcAddr
    or a callable that returns the object that we will use to perform operations against the object.

    init_func is a callable that returns a new vulkan object with the given parameters.

    additional_params is a dictionary of additional values that can be set on the object.
    When a value is set, the method will automatically be called with the new value. So
      additional_params = {'enabled
