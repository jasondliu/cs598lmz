import socket
import sys
import threading
import time
import traceback
import urllib
import urllib2
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn

from oauth import oauth

# The following is a hack to get around the fact that oauth.py doesn't
# support passing in a custom urllib2 opener.
class OAuthRequest(oauth.OAuthRequest):
  def __init__(self, http_method=None, http_url=None, parameters=None,
               consumer=None, token=None, realm=None, verifier=None,
               signature_method=oauth.OAuthSignatureMethod_HMAC_SHA1(),
               callback=None, callback_confirmed=False, opener=None):
    oauth.OAuthRequest.__init__(self, http_method, http_url, parameters,
                                consumer, token, realm, verifier,
                                signature_method, callback, callback_confirmed)
    self.opener = opener

  def to_url(self):
