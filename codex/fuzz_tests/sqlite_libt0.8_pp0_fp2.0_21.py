import ctypes
import ctypes.util
import threading
import sqlite3
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


class User(object):
    def __init__(self, id, firstName, lastName, username, is_bot=False, language_code=None):
        self.id = id
        self.first_name = firstName
        self.last_name = lastName
        self.is_bot = is_bot
        self.username = username
        if language_code is None:
            self.language_code = 'en'
        else:
            self.language_code = language_code

    def __str__(self):
        name = self.first_name
        if self.last_name:
            name += ' ' + self.last_name

        return name + ' [' + str(self.id) + ']'


class Message(object):
    def __init__(self, message_id, from_user
