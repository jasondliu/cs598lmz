import socket

# Constants Load
from galaxy.api.consts import SecureMessageType, LocalGameState
from galaxy.flask.app import GalaxyFlaskInterface
from galaxy.imports import get_namedtuple_from_dict, get_object_from_string
from galaxy.logging import log
from galaxy.socket import GalaxySocketInterface, GalaxySocketManager
from galaxy.time import sleep
from galaxy.util import threaded


class Credentials:
    """
    Object for storing authentication credentials.
    Used for internal authentication.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<Credentials@{self.username}:{self.password}>"

    def to_dict(self):
        """
        Return credentials in dict form.
        """
        return {
            "username": self.username,
            "password": self.password
        }


