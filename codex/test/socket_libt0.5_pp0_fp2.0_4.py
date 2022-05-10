import socket
import sys
import time

from datetime import datetime
from threading import Thread
from typing import List

from pydantic import BaseModel

from utils import get_logger, get_config

logger = get_logger(__name__)

config = get_config()


class Client(BaseModel):
    name: str
    ip: str
    port: int
    socket: socket.socket
    last_ping: datetime


clients: List[Client] = []


def get_client(name: str) -> Client:
    for client in clients:
        if client.name == name:
            return client
    return None


def get_clients() -> List[Client]:
    return clients


def get_clients_online() -> List[Client]:
    return [client for client in clients if client.socket]


def get_clients_offline() -> List[Client]:
    return [client for client in clients if not client.socket]


