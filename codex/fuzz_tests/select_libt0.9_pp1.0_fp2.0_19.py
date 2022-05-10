import select
import time
import traceback

from . import common_interface
from . import interface


class Binding:
    """
    An object that binds a :py:class:`Input` to a function.

    :param Input input: The Input to bind to.
    :param function f: The function to bind to the input.
    :param int key: The keycode of the binding.
    """
    def __init__(self, input, f, key):
        self.input = input
        self.f = f
        self.key = key
        self.g = common_interface.KeyCombination([key])  # TODO: Use a hashable object like a frozenset or a namedtuple.

    def __repr__(self):
        return "Binding({!r}, {!r}, {!r})".format(self.input, self.f, self.key)

    def __call__(self):
        """
        Calls the binding. If a keyboard callback is defined, calls that along with the function.
        """
        if self.input._callback:
            self
