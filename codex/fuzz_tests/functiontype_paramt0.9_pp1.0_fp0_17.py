from types import FunctionType
list(FunctionType(lambda x: 'Hi there', globals(), 'fn-name'))
```

```python
from numbers import Number
list(Number(5))
# Traceback... TypeError: 'Number' object is not iterable
```

```python
from fractions import Fraction
list(Fraction(9, 3))
# []
```

```python
from collections import OrderedDict
list(OrderedDict())
# []
```

**Exercise**: how about immutable mappings, sets and sequences?

---

# Functionality

- Strings, ints, floats, tuples, arrays and other types are iterable because they respond to special methods, just like the iterator.
- The iterator.next(), which calls iterator.__next__(), returns the next item, and raises StopIteration when done.
- An iterable is a type that returns an iterator with the iter() function.
- Iteration protocols are documented in `PEP 234`, *Iterators for Python*.
- `PEP 234` does not specify how built-in types create iterators. Each built-in
