import types
types.ModuleType('m')

import m
m.__name__

# This is a module
m

# This is a module
m.__name__

# This is a module
m.__dict__

# This is a module
m.__dict__['__file__']

# This is a module
m.__dict__['__file__'] = './m.py'

# This is a module
m.__dict__['__file__']

# This is a module
m.__dict__['__name__']

# This is a module
m.__dict__['__name__'] = 'm'

# This is a module
m.__dict__['__name__']

# This is a module
m.__dict__['__package__']

# This is a module
m.__dict__['__package__'] = 'foo'

# This is a module
m.__dict__['__package__']

# This is a module
m.__dict__['__path__']

# This is a module
m.
