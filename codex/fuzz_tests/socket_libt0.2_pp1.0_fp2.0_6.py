import socket
import sys
import time
import threading
import traceback
import urllib
import urllib2
import urlparse
import uuid
import xml.etree.ElementTree as ET

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from xml.dom import minidom

from oauth import oauth

from upnp import UPnP
from upnp import UPnPError
from upnp import UPnPResponseError
from upnp import UPnPTimeoutError

from ssdp import SSDPResponse
from ssdp import SSDPServer

from xbmcswift2 import Plugin
from xbmcswift2 import xbmc
from xbmcswift2 import xbmcaddon
from xbmcswift2 import xbmcgui
from xbmcswift2 import xbmcplugin

from xbmcswift2.logger import log

from xbmcswift2.common import get_local_ip
from xbmcswift2.common import get_local_ipv6
