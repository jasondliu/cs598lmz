import weakref

from typing import Optional, List, Union, cast, Tuple, TYPE_CHECKING

from .. import enums
from .. import settings
from .. import utils
from .. import exceptions
from .. import entities
from .. import data
from .. import logging
from .. import base
from .. import commands
from .. import events
from .. import terminal
from .. import connection

from ..enums import InstanceType, InstanceStatus, InstanceError
from ..enums import InstanceAction, InstanceShutdown
from ..data import Config, InstanceUpdate
from ..logging import Logger
from ..exceptions import DuplicateInstanceError, InvalidInstanceError
from ..protocol import InstanceProtocol, InstanceRequestType
from ..protocol import InstanceResponseType
from ..connection import Connection
from ..connection import ConnectionType
from ..connection import ConnectionProtocol
from ..config import ConfigManager
from ..commands import CommandContext
from ..commands import CommandType
from ..commands import CommandException
from ..commands import CommandError
from ..commands import CommandResponse
