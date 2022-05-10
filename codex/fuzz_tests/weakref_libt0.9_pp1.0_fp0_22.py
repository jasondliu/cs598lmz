import weakref

from anarky.enums import (OPERATOR, TYPE)
from anarky.types.objectpool import ObjectPool
from .. import exception as exc


class Node:
    __slots__ = [
        'type', 'operator', 'arg1', 'arg2', 'arg3', 'parent'
        #'namespace',
        #'_hash'
    ]

    def __init__(self, type, operator=None, arg1=None, arg2=None, arg3=None, parent=None):
        self.type = type
        self.operator = operator
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.parent = parent

    def __repr__(self):
        args = []
        if self.type == TYPE.OPERATOR:
            args.append('operator=%r' % (self.operator))
        if self.arg1 is not None:
            args.append('arg1=%r' % (self.arg1))
        if self.arg2 is not None
