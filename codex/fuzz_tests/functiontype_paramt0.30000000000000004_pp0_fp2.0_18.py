from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# the following is not supported
# list(FunctionType(lambda x: x, globals(), 'lambda', (int,)))

# the following is supported
list(FunctionType(lambda x: x, globals(), 'lambda', (int,), {}))

# the following is supported
list(FunctionType(lambda x: x, globals(), 'lambda', (int,), None))

# the following is supported
list(FunctionType(lambda x: x, globals(), 'lambda', (int,), {'foo': 'bar'}))

# the following is supported
list(FunctionType(lambda x: x, globals(), 'lambda', (int,), {'foo': 'bar'}, None))

# the following is supported
list(FunctionType(lambda x: x, globals(), 'lambda', (int,), {'foo': 'bar'}, 'doc'))

# the following is supported
list(FunctionType(lambda x: x, globals(), 'lambda', (int,), {'foo': 'bar'}, 'doc
