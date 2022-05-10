import weakref

from typing import Any, Callable, Container, Dict, Generic, Iterable, List, \
    Optional, Sequence, Set, Tuple, TypeVar, Union

from macifylinux.constants import Values
from macifylinux.utils.logger import logger
from macifylinux.utils.properties import cached_property, CachedPropertyError, \
    ConfigurableProperty, ConfigurablePropertyAccessError, has_properties
from macifylinux.utils.types import is_string

__all__ = (
    'BaseSetting',
    'BaseSettingTypes',
    'BaseSettingValueScope',
    'BaseSettingValueTypeScope',
    'BaseSettingValueType',
    'BaseGSetting'
)

PValue = TypeVar('PValue')


class BaseSetting(object):
    """The base class for settings."""

    value_type: type
    valid_value: Optional[Container[PValue]] = None
    default_value: Optional[PValue] = None
    deprecated: Optional[Container[PValue]] = None

    @classmethod
    def get_default_value(cl
