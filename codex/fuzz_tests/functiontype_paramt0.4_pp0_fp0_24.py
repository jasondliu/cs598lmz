from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(3))

# list(filter(lambda x: x, [1,0,2,0,3]))

# from itertools import filterfalse
# list(filterfalse(lambda x: x, [1,0,2,0,3]))

# from itertools import compress
# list(compress('ABCDEF', [1,0,1,0,1,1]))

# from itertools import dropwhile
# list(dropwhile(lambda x: x<5, [1,4,6,4,1]))

# from itertools import takewhile
# list(takewhile(lambda x: x<5, [1,4,6,4,1]))

# from itertools import islice
# list(islice('ABCDEFG', 2))
# list(islice('ABCDEFG', 2, 4))
# list(islice('ABCDEFG', 2, None))
# list(islice('ABCDEFG', 0, None, 2))

# from itert
