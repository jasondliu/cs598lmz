from types import FunctionType
list(FunctionType(lambda a: a, globals(), 'lambda') for a in [])
list(FunctionType(lambda a: a, globals(), 'lambda') for a in [1])
list(FunctionType(lambda a: a, globals(), 'lambda') for a in [1, 2])

# List of tuples
list(tuple(map(int, s.split(':'))) for s in ['1:2', '2:3'])

# List of tuples with one element
list(tuple(map(int, s.split(':'))) for s in ['1:2'])

# List of tuples with two elements
list(tuple(map(int, s.split(':'))) for s in ['1:2', '2:3'])

# List of tuples with three elements
list(tuple(map(int, s.split(':'))) for s in ['1:2:3', '2:3:4'])

# List of tuples with four elements
list(tuple(map(int, s.split(':'))) for s in ['
