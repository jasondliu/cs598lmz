import socket
from threading import Thread
from typing import Tuple, List

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from server import Server
from src.common.constants import ServerConstants, ClientConstants
from src.common.utils.message import Message
from src.common.utils.utils import send_message, recv_message


class Client(QObject):
    message_received = pyqtSignal(Message)
    user_list_changed = pyqtSignal(list)

    def __init__(self, host: str, port: str):
        super().__init__()
        self.host = host
        self.port = port
        self.sock = None
        self.server = Server(self.port, self)

    def connect_to_server(self) -> Tuple[bool, str]:
        if self.sock is not None:
            return False, 'You are already connected to server'
        try:
            self.sock = socket.socket()
