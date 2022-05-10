import select
import socket
import sys

from pyftpdlib import ftpserver
from pyftpdlib.handlers import ThrottledDTPHandler
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from .data_providers import DataProvider
from .constants import *
from . import utils


def start_ftp_server(
        port: int = 2121,
        data_provider: DataProvider = None,
        max_speed: int = 0,
        max_cons: int = 0,
        max_cons_per_ip: int = 0,
) -> None:
    """"""
    authorizer = ftpserver.DummyAuthorizer()
    authorizer.add_user(USER, PASSWORD, os.path.realpath(os.curdir), perm='elradfmw')
    authorizer.add_anonymous(os.path.realpath(os.curdir))

    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit = max_
