import _struct
from ftplib import FTP, error_reply, error_temp  # @UnusedImport
from types import NoneType
from traceback import print_exc

from Tribler.Category.Category import Category
from Tribler.Core.Category.FamilyFilter import XXXFilter
from Tribler.Core.CacheDB.CacheDBHandler import TorrentDBHandler
from Tribler.Core.DownloadConfig import DownloadStartupConfig
from Tribler.Core.Session import Session
from Tribler.Core.SessionConfig import SessionStartupConfig
from Tribler.Core.Utilities.utilities import sizeof_fmt, validate_torrent_checksum
from Tribler.Core.simpledefs import (NTFY_ACT_DOWNLOAD, NTFY_ACT_UPDATE, NTFY_ANNOUNCE,
                                     NTFY_DHT_WALKER, NTFY_DHT_LOOKUP, NTFY_MAGNET_CLOSE, NTFY_MAGNET_GOT_PEERS,
                                     NTFY_MAGNET_PROGRESS, NTFY_MAGNET_STARTED, NTFY_MAG
