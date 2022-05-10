import ctypes
ctypes.cast(0, ctypes.py_object)

import os
os.environ["PYTHONPATH"] = ":".join((
    "/usr/local/lib/python2.7/dist-packages/",
    "/usr/lib/python2.7/dist-packages/",
    "/usr/lib/python2.7/",
))

from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import LoopingCall
from twisted.internet.error import CannotListenError
from twisted.protocols.basic import LineReceiver
from twisted.python import log

from jinja2 import Environment, FileSystemLoader
import argparse
import json
import pprint
import socket
import uuid

import speedtest

from cron import Cron
import dns_sd

_template_env = Environment(
    loader=FileSystemLoader("templates"))


class HttpServer(object):
    def __init__(self, config):
        self.config = config
