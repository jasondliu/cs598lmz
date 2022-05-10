import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

import time
import sys
sys.path.append('../../../')

from pysqlite2 import dbapi2 as sqlite

from pyxmpp.utils import to_utf8, from_utf8

from pyxmpp.jabber.client import JabberClient
from pyxmpp.jabber.muc import MucRoomHandler
from pyxmpp.jabber.muc import MucRoom
from pyxmpp.jabber.muc import MucPresence

from pyxmpp.jid import JID
from pyxmpp.message import Message
from pyxmpp.presence import Presence
from pyxmpp.iq import Iq

from pyxmpp.jabber.roster import Roster
from pyxmpp.jabber.roster import RosterItem
from pyxmpp.jabber.roster import RosterItemResource

from pyxmpp.jabber.mood import Mood
from pyxmpp.jabber.tune import Tune
from pyxmpp.jabber
