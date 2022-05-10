from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# list([x for x in range(10)])

# import typing
# list(typing.List[int])

# list(range(2, 3))

list(map(lambda x: x, [1, 2, 3]))

# list(filter(lambda x: x, [1, 2, 3]))

# list(zip(range(10), range(10)))

# list(reversed(range(10)))

# list(enumerate(range(10)))

# list(dict(enumerate(range(10))))

# list(set(range(10)))

# list(frozenset(range(10)))

from collections import deque
list(deque(range(10)))

from collections import defaultdict
list(defaultdict(lambda: None))

from collections import ChainMap
list(ChainMap())

from collections import Counter
list(Counter())

from collections import OrderedDict
list(OrderedDict())

from collections import UserD
