import weakref

from .base import (
    BaseDict,
    BaseList,
    BaseObject,
    BaseSet,
    BaseTuple,
    BaseObjectType,
    JSONType,
    TypeDefinition,
    TypeRegistry,
)
from .types import (
    Any,
    AnyObj,
    Bool,
    Bytes,
    Float,
    Int,
    List,
    Set,
    Str,
    Tuple,
)
from .utils import (
    get_forward_ref_type,
    get_origin,
)


class SerializationError(Exception):
    pass


class DeserializationError(Exception):
    pass


class FrozenDict(BaseDict):
    def __setitem__(self, key, value):
        raise TypeError('FrozenDict is immutable')

