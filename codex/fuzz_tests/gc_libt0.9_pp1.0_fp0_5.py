import gc, weakref ##weakref.WeakSet, weakref.WeakValueDictionary

from .. import enums, events
from ..mixins import EventMixin
from ..ringbuffer import RingBuffer, DropOldestStrategy, DropNewestStrategy

__all__ = (
    'HistoryManager', 'DropNewestHistoryManager', 'DropOldestHistoryManager'
)

##http://stackoverflow.com/questions/6419220/reference-counting-on-a-large-python-object-graph
##http://stackoverflow.com/questions/10263879/python-garbage-collection-aggressive-collection
class HistoryManager (EventMixin): #GarbageCollectorMixin):

    def __init__ (self, source=[], width=0):
        self.buffered = 0
        self.width = width
        self.history = []

        self.set_source(source)

    def on_control(self, key, value):
        if key is enums.Control.ACTIVE:
            if self.source is not None:
                self.source.on_control(key
