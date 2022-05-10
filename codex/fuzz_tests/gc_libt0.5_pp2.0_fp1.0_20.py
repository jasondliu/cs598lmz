import gc, weakref
from collections import defaultdict
from functools import partial
from itertools import chain, starmap
from operator import attrgetter, itemgetter
from weakref import WeakValueDictionary

from . import utils
from .exceptions import (
    BadValueError,
    ConfigurationError,
    DependencyError,
    ExtensionAlreadyLoaded,
    ExtensionNotLoaded,
    MultipleResultsFound,
    NoResultFound,
    UnmappedInstanceError,
    )
from .interfaces import (
    AttributeExtension,
    ClassManager,
    MapperProperty,
    PropComparator,
    SessionExtension,
    SessionTransaction,
    )
from .orm import (
    attributes,
    mapper,
    )
from .orm import strategies
from .orm.base import _entity_descriptor
from .orm.interfaces import (
    AttributeExtensionOption,
    EXT_CONTINUE,
    EXT_STOP,
    MapperProperty,
    PropComparator,
    SessionExtensionOption,
    SessionTransaction,
    )

