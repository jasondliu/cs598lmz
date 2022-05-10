import weakref
from typing import Any, Callable, Generic, GenericMeta, NoReturn, TypeVar

__all__ = [
    "Asyncer",
    "AsyncerFunction",
    "AsyncerMethod",
    "AsyncerProperty",
    "AsyncerUnbound",
]

_T = TypeVar("_T")
_R = TypeVar("_R")


class AsyncerMeta(GenericMeta):
    def __new__(mcs, name: str, bases: Any, attrs: Any) -> Any:
        for base in bases:
            if hasattr(base, "__asyncer_base__"):
                break
        else:
            base = object

        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, Asyncer):
                attr_value.__name__ = attr_name

        return super().__new__(mcs, name, bases, attr_value)


class AsyncerUnbound(Generic[_T]):
    """
    A placeholder for a not
