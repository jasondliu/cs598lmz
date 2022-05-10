import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite

from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols.basic import LineReceiver

from plugins.plugin import Plugin
from plugins.plugin import Config
from plugins.plugin import Command


class Bot(LineReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.nick = factory.nick
        self.realname = factory.realname
        self.username = factory.username
        self.password = factory.password
        self.channels = factory.channels
        self.plugins = factory.plugins
        self.config = factory.config
        self.db = factory.db
        self.db_lock = factory.db_lock
        self.db_cursor = factory.db_cursor

    def connectionMade(self):
        self.sendLine("NICK %s" % self.nick)
        self.sendLine("USER %s 0 * :%s" % (self.username, self.realname))

