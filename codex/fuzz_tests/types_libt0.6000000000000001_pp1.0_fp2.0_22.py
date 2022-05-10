import types
types.__dict__['__builtins__']

# The following is not allowed in Python 3
# import __builtin__
# __builtin__.__dict__['__import__']

# but can be done in Python 2
import __builtin__
__builtin__.__dict__['__import__']

# The following is not allowed in Python 3
# __import__('sys').__dict__['__import__']

# but can be done in Python 2
__import__('sys').__dict__['__import__']

# The following is not allowed in Python 3
# __import__('sys').__import__('os').__dict__['__import__']

# but can be done in Python 2
__import__('sys').__import__('os').__dict__['__import__']

# The following is not allowed in Python 3
# __import__('sys').__import__('os').__import__('types').__dict__['__import__']

# but can be done in Python 2
__import__('sys').__import__('os').__import__('types
