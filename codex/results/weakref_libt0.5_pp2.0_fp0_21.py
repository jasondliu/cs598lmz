import weakref

from .. import config
from .. import constants
from .. import utils
from .. import errors
from .. import events
from .. import enums
from .. import objects
from .. import http
from .. import data_manager
from .. import channel
from .. import abc
from .. import voice_client
from ..voice_client import VoiceClient
from ..enums import Status, ChannelType, try_enum
from ..permissions import Permissions
from ..invite import Invite
from ..user import ClientUser
from ..webhook import Webhook
from .. import compat
from ..audit_logs import AuditLogs
from ..calls import CallMessage

from . import utils as gateway_utils
from . import handlers
from . import state_manager
from . import connection
from . import stream
from . import handlers
from . import compat
from . import payloads
from . import events as gateway_events
from . import errors as gateway_errors
from . import data_manager as gateway_data_manager
from . import abc as gateway_abc

from .payloads import (
    Hello,
    Heartbeat,

