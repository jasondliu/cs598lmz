from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = "bz2"

import sys
import os
import time
import socket
import select
import logging
import cStringIO
import traceback
import threading
import subprocess
import Queue
import urllib2
import httplib
import ssl
import re
import json
import zlib
import base64

from M2Crypto import SSL, httpslib, m2, threading as m2threading
m2.lib(m2.LIB)
m2threading.lib(m2threading.LIB)

from Config import config
from Plugin import PluginManager
from Debug import Debug
from util import helper

log = logging.getLogger("Server")


class Server(object):
    def __init__(self, ip="0.0.0.0", port=config.fileserver_port, ip_v6="::", port_v6=None, ssl=config.fileserver_ssl, ssl_cert=config.fileserver_ssl_cert, ssl_key=config.fileserver_ssl_key, data_dir=config.
