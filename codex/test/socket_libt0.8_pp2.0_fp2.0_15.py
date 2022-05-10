import socket

import netifaces
from smc.base.model import Element, ElementCreator
from smc.base.util import element_resolver
from smc.api.exceptions import CreateElementFailed, ElementNotFound, \
    DeleteElementFailed, UpdateElementFailed, ElementInstanceNotFound
from smc.base.structs import NestedOrderedDict, ElementDiff, \
    ElementEdgeDiff, ElementEdge
from smc.base.structs import EdgeSubInterface
from smc.base.util import get_next_available_edge
from smc.base.decorators import required_if
from smc.api.decorators import make_session, check_session_type


