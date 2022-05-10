import types
types.ModuleType.__init__ = noop

class Module(types.ModuleType):

    @classmethod
    def __getattr__(cls, name):

        if name != '__dict__':
            try:
                return cls.__dict__[name]
            except KeyError:
                pass

        raise AttributeError(
            "'%s' object has no attribute '%s'" % (
                cls.__name__, name))

    @classmethod
    def __setattr__(cls, name, value):

        raise AttributeError(
            "'%s' object attribute '%s' is read only" % (
                cls.__name__, name))

    @classmethod
    def __delattr__(cls, name):

        raise AttributeError(
            "'%s' object attribute '%s' is read only" % (
                cls.__name__, name))

    @classmethod
    def __init__(cls, name, bases, namespace, **kw):

        if '__dict__' in namespace:
            raise Type
