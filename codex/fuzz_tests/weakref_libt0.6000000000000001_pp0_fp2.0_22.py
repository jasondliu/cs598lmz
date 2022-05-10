import weakref

import numpy as np

from .dispatcher import Dispatcher
from .event import Event
from .event_hook import EventHook
from .monitor import Monitor
from .node import Node
from .node_meta import NodeMeta
from .task import Task


# TODO:
#  - Add more details to the `__repr__` string.
#  - Add support for specifying the `dtype` of a `Node`.
#  - Add support for specifying the `shape` of a `Node`.
#  - Add support for `Node`s which are containers (lists, dicts, etc).
#  - Add support for `Node`s which are iterables.
#  - Add support for `Node`s which are generators.
#  - Add support for `Node`s which are callables.
#  - Add support for `Node`s which are `Monitor`s.
#  - Add support for `Node`s which are `EventHook`s.
#  - Add support for `Node`s which are `Task`s.
#  - Add support for `Node`s
