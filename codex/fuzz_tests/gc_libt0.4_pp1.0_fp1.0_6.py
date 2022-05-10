import gc, weakref
import traceback
import logging

from twisted.internet import reactor, defer
from twisted.internet.defer import Deferred, DeferredList, maybeDeferred

from zope.interface import implements

from deluge.core.rpcserver import export
from deluge.core.torrent import Torrent
from deluge.core.torrentmanager import TorrentManager

from deluge.event import DelugeEvent
import deluge.component as component

from deluge.interfaces import ITorrentManager

log = logging.getLogger(__name__)

class CoreTorrentManager(TorrentManager):
    def __init__(self):
        TorrentManager.__init__(self)

        self.torrents = {}
        self.torrents_status_keys = []
        self.torrents_status_keys_default = []
        self.torrents_status_keys_extended = []

        # This is used to keep track of the torrents that have been added
        # to the session, but not yet saved to the state file.
        self.torrents_pending_
