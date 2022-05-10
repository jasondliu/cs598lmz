import weakref
from functools import wraps
from inspect import signature
from typing import Any, Callable, Generic, Iterable, Sequence, Type, TypeVar

from .caching import CachingMixin
from .errors import (
    AlreadyExists,
    DoesNotExist,
    MissingDependency,
    MultipleArgumentError,
    MultipleDependencyError,
    NoneFactoryError,
    NullFactoryError,
    NullInjectionError,
    OverriddenArgumentError,
    OverriddenBindingsError,
    OverriddenInjectableError,
    OverriddenKeyError,
    OverriddenTaggedError,
    UnboundDependency,
)
from .injectable import Injectable
from .injection_context import DEFAULT_CONTEXT, InjectionContext
from .injector import Injector
from .key import (
    DefaultAnnotation,
    DefaultKey,
    Key,
    NoAnnotation,
    NullKey,
    TaggedKey,
    unique_key,
)
from .records import BindingRecord


