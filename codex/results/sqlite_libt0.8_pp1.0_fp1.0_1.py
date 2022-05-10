import ctypes
import ctypes.util
import threading
import sqlite3
import codecs
import struct
import socket
import getopt
import sys
import os
import signal
import hashlib
import base64
import logging
import threading
import tempfile
import urllib
import time
import webbrowser

# python-urwid is available at
# http://excess.org/urwid
import urwid as ur

# libmDNSPlugin.dylib is available at
# http://trac.macosforge.org/projects/libdns_sd/
dns_sd_lib = ctypes.CDLL(ctypes.util.find_library('dns_sd'))

class ServiceBrowser(object):
    def __init__(self, _services, _resolver):
        self.services = _services
        self.resolver = _resolver

    def add_service(self, _name, _type, _domain):
        """ Called by DNSServiceBrowse when a new service has been found """
        self.services.add_service(_name, _type, _domain)
        self.resolver.resolve_service(_name,
