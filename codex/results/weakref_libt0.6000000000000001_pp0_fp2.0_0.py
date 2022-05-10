import weakref
import copy

from typing import Any, Dict, Set, List, Optional, Union, Callable, Iterable, Iterator
from typing_extensions import Literal
from typing import cast

from .datatypes import DictType, SetType, ListType, \
    OptionalType, UnionType, CallableType, IterableType, \
    IteratorType, AnyType, Type, TypeType, TypeTypeType, \
    TypeOfType, LiteralType, TupleType, ForwardRefType, \
    TypeReference, TypeVariable, TypeVars, TypeVarType, \
    ClassVarType, NewTypeType, NewType, NewTypeTypeType, \
    ListMetaType, SetMetaType, DictMetaType, TupleMetaType, \
    DeletedType
from .utils import is_generic_type, is_named_tuple, is_union_type, \
    is_callable_type, is_new_type, is_function_type, is_literal_type, \
    is_type_of_type, is_type_type, is_type_type_
