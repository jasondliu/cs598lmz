import weakref
from collections import defaultdict
from importlib import import_module
from inspect import signature
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Mapping,
    MutableMapping,
    NamedTuple,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)

from indy_common.config_util import getConfig
from plenum.common.constants import CURRENT_PROTOCOL_VERSION
from plenum.common.messages.fields import IdentifierField, NonNegativeNumberField
from plenum.common.timer import QueueTimer
from plenum.common.types import f
from plenum.server.suspicion_codes import Suspicions

from anoncreds.protocol.types import ID, RevocationRegistry, Schema
from indy_client.agent.agent import Agent
from indy_client.agent.runnable import Runnable
from indy_common.constants import REVOC_REG_DEF, GET_REVOC
