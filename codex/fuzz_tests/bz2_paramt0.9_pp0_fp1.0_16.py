from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = BZ2Decompressor.decompress_async = lambda self, data: self.decompress(data)

from aio_pika import connect, Message, DeliveryMode, ExchangeType
from aio_pika import exceptions
from aiohttp import web
import yaml
import os
import logging
import asyncio
import jwt
import json

log = logging.getLogger("api")
log.level = logging.DEBUG
log.addHandler(logging.StreamHandler())

os.environ["PYTHONASYNCIODEBUG"] = "1"

# Load configuration
with open('config.yml', 'r') as stream:
    config: dict
    config = yaml.safe_load(stream)


class ConsumerClient:
    """Singleton class providing some abstraction over RabbitMQ connection & queue subscriptions """

    _instance = None
    _connections = {}
    _channels = {}
    _pending_tasks = []

    def __new__(cls):
        if cls._instance is None:
            cls._
