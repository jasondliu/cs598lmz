import types
types.MethodType(lambda self: self.name, '', '', '')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MethodType(object):
    def __init__(self, method, instance, cls):
        self.method = method
        self.instance = instance
        self.cls = cls

    def __call__(self, *args, **kwargs):
        return self.method(self.instance, *args, **kwargs)

    def __repr__(self):
        return 'MethodType({}, {}, {})'.format(self.method, self.instance, self.cls)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MethodType(object):
    def __init__(self, method, instance, cls):
        self.method = method
        self.instance = instance
        self.cls = cls

    def __call__(self, *args, **kwargs):
        return self.method(self.instance, *args, **kwargs)

    def __repr__(self):
        return 'MethodType({}, {}, {}
