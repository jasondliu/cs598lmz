import types
# Test types.FunctionType fails on python 3.
if sys.version_info.major < 3:
    from types import FunctionType


# functools.update_wrapper also available in python 2.4+
def update_wrapper(wrapper: types.FunctionType,
                   wrapped: types.FunctionType,
                   assigned=functools.WRAPPER_ASSIGNMENTS,
                   updated=functools.WRAPPER_UPDATES) -> types.FunctionType:
    """Update the attributes of a callable to those of another callable.

    The ``wrapper`` callable will have the same signature as the
    ``wrapped`` callable, but all of its attributes will be either
    inherited or updated from the ``wrapped`` callable.  This is useful
    for creating decorators that will remain unchanged from those of
    the functions they decorate.

    ``assigned`` is a list of attribute names that will be copied from
    the ``wrapped`` callable to the ``wrapper`` callable.  By default,
    this is WRAPPER_ASSIGNMENTS.  ``updated`` is a list of attribute
    names that will be
