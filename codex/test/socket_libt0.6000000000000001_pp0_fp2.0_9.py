import socket
import urllib
import urllib2
import urlparse
import json

#socket.setdefaulttimeout(30)

class EvernoteSession(object):
    """EvernoteSession class."""

    def __init__(self, key, secret, sandbox=False):
        """Constructor of EvernoteSession class.

        Args:
            key: Consumer key for your application.
            secret: Consumer secret for your application.
            sandbox: If True, use sandbox server.

        """
        self.key = key
        self.secret = secret
        self.sandbox = sandbox
        self.token = None
        self.auth_url = '%s/OAuth.action' % self.base_url

    @property
    def base_url(self):
        """Base URL of Evernote API.

        Returns:
            Base URL.

        """
        if self.sandbox:
            return 'https://sandbox.evernote.com'
        else:
            return 'https://www.evernote.com'

