import socket
import sys
import time

from src.common.constants import *
from src.common.logger import Logger
from src.common.utils import *
from src.common.config import Config
from src.common.message import Message
from src.common.message_type import MessageType

from src.server.server_state import ServerState
from src.server.server_state_machine import ServerStateMachine

from src.server.server_state_initial import ServerStateInitial
from src.server.server_state_ready import ServerStateReady
from src.server.server_state_waiting import ServerStateWaiting
from src.server.server_state_running import ServerStateRunning
from src.server.server_state_finished import ServerStateFinished

from src.server.server_state_error import ServerStateError

class Server:
    def __init__(self, config):
        self.config = config
        self.logger = Logger(self.config.log_file)
        self.state_machine = ServerStateMachine(self)

        self.state_machine.add_
