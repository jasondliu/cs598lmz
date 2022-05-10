import ctypes
import ctypes.util
import threading
import sqlite3
import os
import json

from nucleon.amqp import Connection
from nucleon.amqp import Exchange
from nucleon.amqp import Channel

# SQLITE3
DB = 'qpid.db'

# AMQP
RABBITMQ = 'amqp://nucleon:plop@127.0.0.1:5672/%2F'
EXCHANGE_NAME = 'certification'
EXCHANGE_TYPE = 'topic'

def cleanup_db():
    os.remove(DB)

def init_db():
    """
    initalize the sqlite3 database if it doesn't exists.
    """
    if os.path.exists(DB):
        os.remove(DB)

    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE queue(name TEXT)")
    c.execute("CREATE TABLE result(cert TEXT)")
    c.commit()
    c.close()


