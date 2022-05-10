import socket
from threading import Thread
from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal, QObject

from src.common.constants import *
from src.common.utils import *
from src.common.exceptions import *
from src.common.logger import *


class ClientThread(QThread):
    """
    Класс потока клиента.
    Принимает сообщения от сервера и вызывает сигналы для обновления интерфейса.
    """
    user_list_updated = pyqtSignal(list)
    message_received = pyqtSignal(str, str)

    def __init__(self, client):
        super().__init__()
        self.client = client

   
