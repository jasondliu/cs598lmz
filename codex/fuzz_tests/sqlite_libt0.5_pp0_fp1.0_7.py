import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import subprocess
import signal
import re
import socket
import datetime
import logging
import logging.handlers
import argparse
import json
import traceback
import uuid
import base64

import pyrad.dictionary
import pyrad.packet
import pyrad.tools
import pyrad.client
import pyrad.server

from pyrad.client import Client
from pyrad.dictionary import Dictionary
from pyrad.packet import AccessRequest, AccessAccept, AccessReject, AccountingRequest
from pyrad.server import Server, RemoteHost, RemoteHostIP
from pyrad.server import ServerPacketError
from pyrad.tools import dict_to_dict

from . import config
from . import config_file
from . import database
from . import syslog
from . import util
from . import radius
from . import ipc

def main():
    parser = argparse.ArgumentParser(prog='wifidog-ng')
    parser.add_argument('-c', '--config',
