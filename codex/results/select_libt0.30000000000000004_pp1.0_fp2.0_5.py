import select
import socket
import sys
import threading
import time

from . import __version__
from . import constants
from . import errors
from . import events
from . import utils
from . import voice_client
from . import voice_ws
from .enums import ChannelType
from .enums import Status
from .enums import VoiceRegion
from .gateway import Gateway
from .http import HTTPClient
from .models import Game
from .models import Message
from .models import Server
from .models import User
from .models import VoiceState
from .player import AudioSource
from .player import FFmpegPCMAudio
from .player import Player
from .player import StreamPlayer
from .player import YTDLSource

log = logging.getLogger(__name__)


class Client(object):
    """Represents a client connection that connects to Discord.

    This class is used to interact with the Discord WebSocket and API.

    A number of options can be passed to the :class:`Client`.

    Parameters
    -----------
    max_messages: Optional[:class:`int`]

