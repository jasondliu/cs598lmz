import selectors
import sys
import types

class Action:
    def __init__(self, selector, key, mask):
        self.selector = selector
        self.key = key
        self.mask = mask
        self.handler = None
        self._callback = None

    def __str__(self):
        return '<{}: selector={}, key={}, mask={}, handler={}>'.format(
            self.__class__.__name__, self.selector, self.key,
            sel.EVENT_NAMES[self.mask], self.handler)

    def set_handler(self, handler):
        if not callable(handler):
            raise TypeError
        self.handler = handler
        self._callback = handler()

    def callback(self):
        return self._callback

    def process(self):
        self._callback()


class EventLoop:
    def __init__(self):
        self.selector = selectors.DefaultSelector()
        self.actives = []
        self._stopped = False

