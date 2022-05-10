import select
import socket
import sys
import time
import threading
import os
import signal

from . import config
from . import constants
from . import log
from . import message
from . import utils
from . import vpn

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <config file>" % sys.argv[0])
        sys.exit(1)

    config_file = sys.argv[1]
    config.load(config_file)

    if config.get("log.file"):
        log.set_file(config.get("log.file"))

    log.info("Starting %s" % config.get("app.name"))

    if config.get("app.daemonize"):
        utils.daemonize()

    if config.get("app.pidfile"):
        utils.write_pidfile(config.get("app.pidfile"))

    if config.get("app.user"):
        utils.switch_user(config.get("app.user"))

    signal
