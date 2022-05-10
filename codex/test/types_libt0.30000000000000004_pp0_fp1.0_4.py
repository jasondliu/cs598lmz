import types
types.ModuleType.__repr__ = lambda self: self.__name__

# The version of the wrapped module.
__version__ = '1.0.0'

# The semantic version of the module.
__semantic_version__ = '~1.0'

# The author of the wrapped module.
__author__ = 'Miguel Ramos Pernas'

# The email for the author.
