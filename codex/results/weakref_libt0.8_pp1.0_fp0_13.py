import weakref
from contextlib import contextmanager
from functools import partial
from abc import ABCMeta, abstractmethod
from collections import defaultdict
import uuid
from twisted.internet.defer import Deferred


class Event(object):
    """
    A description of a change which may have taken place in a node hierarchy.

    @param node: the node which generated this event.
    @type node: Node

    @param origin: the node whose descendants have changed.
    @type origin: Node

    @param related: a node which is related to this event.
    @type related: Node

    @param attr: the attribute name which changed (if applicable).
    @type attr: str
    """

    def __init__(self, node, related=None, origin=None, attr=None):
        self.node = node
        self.origin = origin if origin is not None else node
        self.related = related
        self.attr = attr

    def clone(self, *newargs, **newkwargs):
        """
        Return a clone of this event with optional overrides.
       
