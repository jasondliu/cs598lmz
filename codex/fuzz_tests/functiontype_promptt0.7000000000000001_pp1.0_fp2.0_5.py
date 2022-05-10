import types
# Test types.FunctionType
try:
	types.FunctionType
except AttributeError:
	raise ImportError('requires types.FunctionType')

# Test exceptions
try:
	import exceptions
except ImportError:
	raise ImportError('requires exceptions')

# Test built-in function 'apply'
try:
	apply
except NameError:
	raise ImportError('requires built-in apply() function')

# Test built-in function 'hasattr'
try:
	hasattr
except NameError:
	raise ImportError('requires built-in hasattr() function')

# Test built-in function 'map'
try:
	map
except NameError:
	raise ImportError('requires built-in map() function')

# Test built-in function 'getattr'
try:
	getattr
except NameError:
	raise ImportError('requires built-in getattr() function')

# Test built-in function 'reduce'
try:
	reduce
except NameError:
	raise ImportError('requires built-in reduce() function')

# Test built-in function 'zip'
try:
