import weakref

ENCODING = "utf-8"

class Event(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return 'Event(%s, %s, %s)' % (self.name, self.args, self.kwargs)


class EventManager(object):
    def __init__(self):
        self._listeners = {}

    def __del__(self):
        self.stop()

    def stop(self):
        self._listeners = {}

    def add_listener(self, name, listener):
        if name not in self._listeners:
            self._listeners[name] = []
        self._listeners[name].append(listener)

    def remove_listener(self, name, listener):
        if name not in self._listeners:
            return
        if listener not in self._listeners[name]:
            return
        self._listeners
