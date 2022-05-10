import weakref

from datetime import datetime

class TrackablePersistenceManager(PersistenceManager):
    """
    A persistence manager that records every instance that gets put into it --
    useful for unit tests.
    """
    def __init__(self):
        PersistenceManager.__init__(self)
        self._counters = defaultdict(int)
        self._objects = {}

    def add(self, obj, value=0):
        PersistenceManager.add(self, obj)
        if not isinstance(obj, basestring):
            self._counters[obj.__class__] += 1
            self._objects[obj] = value

    def delete(self, obj):
        if isinstance(obj, basestring):
            PersistenceManager.delete(self, obj)
        else:
            obj.delete()

    def flush(self, *args):
        pass

class TrackablePersistenceManagerTests(unittest.TestCase):
    """
    Tests for L{TrackablePersistenceManager}.
    """
    def setUp(self):
        self
