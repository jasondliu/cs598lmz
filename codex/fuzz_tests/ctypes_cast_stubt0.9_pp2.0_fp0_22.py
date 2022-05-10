import ctypes
ctypes.cast(address, ctypes.py_object).value
>> [ 1, 2, 3 ]
```

## 内存池

```python
>>> import sys
>>> sys.getsizeof([1, 2, 3, 4, 5])
152
>>> sys.getsizeof([1, 2, 3, 4, 5] * 2)
304

>>> from sys import getsizeof as gs, stderr
>>> from itertools import chain
>>> from collections import deque

>>> def total_size(o, handlers={}, verbose=False):
...    """ Returns the approximate memory footprint an object and all of its contents.

...    Automatically finds the contents of the following builtin containers and
...    their subclasses:  tuple, list, deque, dict, set and frozenset.
...    To search other containers, add handlers to iterate over their contents:

...        handlers = {SomeContainerClass: iter,
...                    OtherContainerClass: OtherContainerClass.get_elements}

...    """
...    dict_handler = lambda d: chain.from_
