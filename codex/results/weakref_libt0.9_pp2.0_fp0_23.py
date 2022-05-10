import weakref
from collections import defaultdict, OrderedDict, Counter, namedtuple
from typing import Dict, List, Set, FrozenSet, Optional, Any, Tuple, Union, Callable, Iterable, NamedTuple 
from typing import NewType, TypeVar, Type, Hashable
from abc import ABC, abstractmethod, ABCMeta
"""
class DeclarativeMeta(type): 
    ...
    # https://hackernoon.com/coding-with-clarity-declarative-python-with-type-hints-1a2706efa6af

    def __new__(cls: Type[T], name: str, bases: Tuple[Type, ...], namespace: Dict[str, Any]) -> Type[T]:
        print("In base DeclarativeMeta's __new__")
        return super().__new__(cls, name, bases, dict(namespace))
"""
"""
    def __new__(cls: Type[T], name: str, bases: Tuple[Type, ...], namespace: Dict[str, Any]) -> Type[T]:
       
