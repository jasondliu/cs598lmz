import gc, weakref
import logging


# TODO:
# - document the "return callable" thing more
# - more tests

# TODO:
# - document the "return callable" thing more
# - more tests


class NoSuchVariableError(Exception):
    pass


class VariableNotSetError(Exception):
    pass


class VariableAlreadySetError(Exception):
    pass


def _wrap_error(thing, errorclass):
    def f(*args, **kwargs):
        try:
            return thing(*args, **kwargs)
        except errorclass:
            return False
    return f


def _return_callable(callable):
    return callable


class _LazyVariable(object):
    """
    A lazy variable. We're storing the variable in a closure
    here, so that if it's a mutable object, we are working
    with the same object every time, not a new copy.
    """
    def __init__(self, variable, variable_name):
        self.variable = variable
        self.variable_name = variable_name
        self
