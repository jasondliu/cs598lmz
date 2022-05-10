import socket

from ConfigParser import ConfigParser

from os.path import expanduser
import os

from lxml import objectify, etree
from lxml.builder import E

from simplejson import dumps, loads

from twisted.web import resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor, threads
from twisted.python import log

from wokkel import data_form
from wokkel import muc
from wokkel import pubsub as wokkel_pubsub
from wokkel import xmppim

from eridanusstd import eridanus
from eridanusstd.comic import Comic, ComicNotFound


## Path to pid file
pidfile = os.path.join(os.getcwd(), "irccat.pid")

## IRC channel to announce to
channel = "#eridanus"

## XMPP muc to announce to
muc_jid = u"eridanus@conference.eridanus.org"
muc_nick = u"eridanus-bot"
muc_password = u"er
