from types import FunctionType
list(FunctionType(lambda x: x+1, {}, None, None, None)(1))

# AttributeError: 'int' object has no attribute 'append'
# https://docs.python.org/3/library/functions.html#func-dir
dir(1)
dir(int)

# https://docs.python.org/3/library/functions.html#func-hash
# https://docs.python.org/3/library/functions.html#func-help
# https://docs.python.org/3/library/functions.html#func-hex
# https://docs.python.org/3/library/functions.html#func-id
# https://docs.python.org/3/library/functions.html#func-oct

# https://docs.python.org/3/library/functions.html#func-chr
chr(1)

# https://docs.python.org/3/library/functions.html#func-ord
ord('1')

# https://docs.python.org/3/library/functions.html#
