import socket
import sys
import json
import logging
import re
import ssl
import pprint
import subprocess
import ConfigParser
import os
import time
import unicodedata

from pprint import pprint

import requests

from Queue import Queue
from threading import Thread
from threading import current_thread
from requests.auth import HTTPBasicAuth

class BOT:

    def __init__(self):

        self.HOST = 'irc.freenode.net'
        self.PORT = 6667
        self.NICK = 'xmpp.bot'
        self.REALNAME = 'xmpp.bot'
        self.IDENT = 'xmpp.bot'
        self.CHANNEL = '#xmpp.bot'
        self.PASSWORD = 'password'
        self.read_config()

        self.database = 'db'
        self.read_config()

