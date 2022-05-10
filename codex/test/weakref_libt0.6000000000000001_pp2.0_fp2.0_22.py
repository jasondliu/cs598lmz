import weakref
from typing import Union, Optional, List, Tuple, Any, Callable, Iterator, TypeVar, Generic, Dict, Type, Set, overload
from typing import Protocol, GenericMeta, cast

from .cgutils import is_struct
from .errors import TypingError, UntypedAttributeError
from .templates import AttributeTemplate
from .typeof import typeof
from .types import (
    Type, Any, Optional, List, Tuple, Union, Dict, Set, FrozenSet, Iterator,
    TypeVar, Callable, T, U, K, V, S, T_co, V_co,
)

