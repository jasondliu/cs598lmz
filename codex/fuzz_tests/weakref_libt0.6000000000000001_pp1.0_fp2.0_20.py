import weakref

from . import utils


class State:
    """
    A state of the finite state machine.

    States are created using the :func:`add_state` factory function.
    """

    __slots__ = ("_machine", "name", "on_enter", "on_exit", "ignore")

    def __init__(self, machine, name, on_enter=None, on_exit=None, ignore=None):
        self._machine = weakref.ref(machine)
        self.name = name
        self.on_enter = on_enter
        self.on_exit = on_exit
        self.ignore = ignore

    def __str__(self):
        return self.name


def add_state(machine, name, on_enter=None, on_exit=None, ignore=None):
    """
    Add a state to the machine.

    :param machine: The :class:`Machine` instance.
    :param name: The name of the state.
    :param on_enter: A callback that is executed when the state is entered.
    :param
