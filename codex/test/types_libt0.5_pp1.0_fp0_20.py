import types
types.ModuleType.__path__ = ['']

# Classes

class Namespace(object):
    '''
    A namespace is a mapping from names to values.

    A namespace can be imported from a module.  The module is
    searched to find an attribute by that name, which can either be
    an object or another module (or package).  If that attribute is
    another module (or package), then the namespace continues to be
    filled from that module.

    Namespaces can be created manually by passing in a mapping of
    names to values.  Namespaces can also be created by passing in a
    list of modules or other namespaces.

    Namespaces are mutable.  They also have a copy method that creates
    a shallow copy of the namespace.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor.

        @param args A list of modules or other namespaces to import
        from.

        @param kwargs A mapping of names to values.
        '''
        self.__dict__ = dict()
