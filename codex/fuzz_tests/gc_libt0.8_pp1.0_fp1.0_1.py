import gc, weakref

from .keywords import KEYWORDS
from .types import NULL, UNDEFINED, INT, DOUBLE, STRING, OBJECT, HASH
from .object import Object, NativeFunction

class Base(object):
    def __init__(self):
        self.register('print', print)
        self.register('gc', gc)
        self.register('eval', NativeFunction(self.eval))
        self.register('typeof', NativeFunction(typeof))
        self.register('new', NativeFunction(self.new))
        self.register('instanceof', NativeFunction(instanceof))
        self.register('length', NativeFunction(self.length))
        self.register('set', NativeFunction(self.set))
        self.register('get', NativeFunction(self.get))
        self.register('del', NativeFunction(self.del_var))
        self.register('call', NativeFunction(self.call))
        self.register('apply', NativeFunction(self.apply))
        self.register('hasattr', NativeFunction(self.hasattr))
        self.
