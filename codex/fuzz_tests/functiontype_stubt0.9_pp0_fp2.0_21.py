from types import FunctionType
a = (x for x in [1])
type(a)

from types import FunctionType
from collections import Iterator

isinstance(abs, FunctionType)

from types import FunctionType
from collections import Iterator

a = isinstance(map, FunctionType)
b = isinstance('map', Iterator)
isinstance(map, Iterator)

from types import FunctionType
from collections import Iterator

a = isinstance(map, FunctionType)
b = isinstance('map', Iterator)
c = isinstance(iter(map), Iterator)

from types import FunctionType
from collections import Iterator

a = isinstance(map, FunctionType)
b = isinstance('map', Iterator)
c = isinstance(iter(map), Iterator)
print(a and not b and not c)

from types import FunctionType
from collections import Iterator

a = isinstance(map, FunctionType)
b = isinstance('map', Iterator)
c = isinstance(iter(map), Iterator)
print(a and b and c)

 
print(a or b or c)

 
print
