import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from BeautifulSoup import BeautifulSoup

import config
import utils

class BasePlugin(object):
    """
    Base class for all plugins.
    """

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
        self.db = bot.db
        self.irc = bot.irc
        self.name = self.__class__.__name__
        self.regex = re.compile(r'^\s*\.%s(?:\s+|$)(.*)' % self.name, re.I)
        self.url_regex = re.compile(r'(https?://[^\s]+)')

    def on_pubmsg(self, source, target, msg):
        """
        Called when we get a message.
        """
        if not self.regex.match(msg):
            return

        try:
            self.handle_
