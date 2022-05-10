import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import Error

from . import config
from . import util
from . import db
from . import model
from . import logger

from .model import *
from .db import *

logger = logger.get_logger('i3-workspace-switch')

def main():
    logger.info('Starting i3-workspace-switch.')
    logger.debug('Parsing command line arguments.')
    args = parser.parse_args()
    config.load_config(args)
    logger.debug('Config:\n%s', config.Config.config)
    logger.debug('Command line arguments:\n%s', args)

    # initialize i3ipc
    logger.debug('Initializing i3ipc connection.')
    i3 = i3ipc.Connection()

    # initialize dbus connection
    logger.debug('Initializing dbus connection.')
    bus = dbus.SessionBus()
    obj = bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')
    notify =
