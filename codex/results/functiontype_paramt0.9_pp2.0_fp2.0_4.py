from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'name') for i in range(10))
#[<function name at 0x7f177b8e0510>, <function name at 0x7f177b8e0678>, ...]
```


## `singleton`

Creates a single object matching some condition

### Parameters

#### `fn`

A function creating the object.

#### `*args`

Arguments for the creating function.

#### `**kwargs`

Named arguments for the creating function.

#### `**cache`

Cache for searching for objects.

### Returns

The object.

### Example

```python
from machinable import Component
from machinable.singleton import singleton
from machinable import Mixin


class Dummy(Component):
    @singleton
    def create_dummy(self) -> Mixin:
        # creates only a single instance
        return Mixin()


```


## `Singleton`

Class to which a single object is bound.

### Example


