import select
import socket
import sys
import traceback
import json
import zmq
from zmq.eventloop.zmqstream import ZMQStream
import time
import os

from sqlalchemy import create_engine, and_, func
from sqlalchemy.orm import sessionmaker

from nymms.reactor import Reactor
from nymms.utils import get_logger, get_lockfile
from nymms.transport import Transport
from nymms.scheduler import Scheduler
from nymms import results
from nymms.objects import State

from nymms.config import config as yaml_config

import nymms.utils.pgp_utils


class Daemon(object):
    def __init__(self, name, config_file=None, config=None):
        self.name = name
        self.config = config
        self.logger = None
        self.lockfile = None
        self.config_file = config_file
        self.sessions = {}
        self.results_session = None
        self.transport =
