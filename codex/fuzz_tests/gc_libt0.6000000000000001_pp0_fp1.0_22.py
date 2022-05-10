import gc, weakref
from collections import OrderedDict

class Rule(object):
    def __init__(self, name, callback, args, kwargs):
        self.name = name
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.done = False
        self.dependencies = set()
        self.dependents = set()
        self.__weakref__ = weakref.ref(self)

    def __str__(self):
        return '<Rule %s>' % self.name

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.name)

class RuleEngine(object):
    def __init__(self):
        self.rules = {}
        self.dependencies = {}
        self.runnable = OrderedDict()

    def rule(self, name, dependencies=()):
        def decorator(callback):
            self.add_rule(name, callback, dependencies)
            return callback
        return decorator

   
