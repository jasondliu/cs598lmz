from types import FunctionType
list(FunctionType(1, 2))

# Token(type=1, value='list', start=(1, 0), end=(1, 4), line='list     (FunctionType  (1,                2))')
list([FunctionType(1, 2)])

# Token(type=1, value='list', start=(1, 0), end=(1, 4), line='list     ([FunctionType(1,                2)])')
list({FunctionType(1, 2): 1, 'b': 2})

# Token(type=1, value='list', start=(1, 0), end=(1, 4), line='list     ({FunctionType(1,                2):1, \'b\':2})')
# Token(type=6, value='dict', start=(1, 8), end=(1, 12), line='list     ({FunctionType(1,                2):1, \'b\':2})')
# Token(type=4, value='dict_display', start=(1, 7), end=(1, 15), line='list     ({FunctionType(1,                2):1, \'b\':2})')
#
