import select
import sys
import threading
import time
import traceback
import urllib
import urlparse

import pika

from django.conf import settings

from . import log
from . import models
from . import utils


class Worker(object):
    """
    Worker class that runs in a thread and handles all the work.
    """

    def __init__(self, queue, connection, channel, queue_name,
                 exchange_name, routing_key, exchange_type, prefetch_count):
        self.queue = queue
        self.connection = connection
        self.channel = channel
        self.queue_name = queue_name
        self.exchange_name = exchange_name
        self.routing_key = routing_key
        self.exchange_type = exchange_type
        self.prefetch_count = prefetch_count
        self.should_stop = False
        self.logger = log.get_logger(__name__)

