import threading
threading._DummyThread._Thread__stop = lambda x: 42

import sys
import os
from time import time

from configparser import ConfigParser
from irc.client import NickMask, IPV4Address, IPV6Address, SimpleIRCClient

from nete import utils
from nete.components.chat import ChatComponent
from nete.components.task import TaskComponent
from nete.state import State
from nete.storage.sqlite_storage import SqliteStorage

class IrcBot(SimpleIRCClient):

    def __init__(self, settings, storage):
        SimpleIRCClient.__init__(self)
        self.settings = settings
        self.storage = storage
        self.state = State(self.storage, settings.get('ircbot', 'nick'))
        self.last_activity_time = None
        self.last_activity_nick = None
        self.last_activity_channel = None
        self.components = {
            'chat': ChatComponent(self.state, settings),
            'task': TaskComponent(self.state, settings)

