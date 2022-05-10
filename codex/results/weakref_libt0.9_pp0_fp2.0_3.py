import weakref

from . import utils


class Navigator:
    def __init__(self, xbar):
        self.xbar = weakref.ref(xbar)
        self.navigate = {}
        self.states = {}
        self.current = None

    def set_state(self, state):
        """Set the navigation state of the xbar to the given one."""
        self.xbar().state = state
        for func in self.navigate.get(state, []):
            func()

    def assert_state(self, state):
        """Set the navigation state of the xbar back to our desired one.

        If it's already there, don't do anything.

        If the user changes state, this needs to be called again.
        """
        if self.xbar().state != state:
            self.set_state(state)

    def register_navigate(self, state, func):
        """Add the given function to the list of functions to call when the
        xbar navigates to the given state.
        """
        self.assert_state(self.
