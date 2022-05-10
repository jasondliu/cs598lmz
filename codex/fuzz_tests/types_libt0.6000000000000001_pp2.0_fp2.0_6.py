import types
types.new_class('Foo')

from types import new_class
new_class('Foo')

from types import new_class as new_class
new_class('Foo')

from types import (
    new_class
)
new_class('Foo')

from types import (
    new_class,
    new_function,
)
new_class('Foo')
new_function('bar')

from types import (
    new_class as new_class,
    new_function as new_function,
)
new_class('Foo')
new_function('bar')

from types import (
    new_class,
) as types
types.new_class('Foo')

from types import (
    new_class as new_class,
) as types
types.new_class('Foo')

from types import (
    new_class,
    new_function,
) as types
types.new_class('Foo')
types.new_function('bar')

from types import (
    new_class as new_class,
