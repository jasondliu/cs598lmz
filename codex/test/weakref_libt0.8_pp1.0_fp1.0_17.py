import weakref

from . import BaseSpecial, NoNodes
from .exceptions import BlockSyntaxError


__all__ = ('Value', 'filter_or_reject', 'filter', 'reject')


