import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import traceback
import socket
import signal

import log
import net
import env
import osinfo
import updates
import system

CMD_HOST = 'localhost'
CMD_PORT = 9200

login_logs = {}
login_log_lock = threading.Lock()

init_complete = False
init_complete_lock = threading.Lock()

# required by _wait_init
init_thread = None
init_done = threading.Event()

def _wait_init():
    global init_done

    if init_complete:
        return

    # wait for initialization of updater
    init_thread.join()
    init_done.wait()

def _acct_id(name):
    return net.user_domain_name(name)

def _host_id(host):
    # TODO: implement this as a UUID
    host = host.lower()
    h = hashlib.new('md5')
    h.update(host)
    return h.hexdigest().lower()

def _init
