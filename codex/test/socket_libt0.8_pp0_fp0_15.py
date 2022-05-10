import socket
from time import time, sleep
from traceback import print_exc
import string

from Tribler.Core.Utilities.bencode import bencode, bdecode
from Tribler.Core.simpledefs import *
from Tribler.Core.CacheDB.sqlitecachedb import bin2str, str2bin, SQLiteCacheDB
from Tribler.Core.Utilities.utilities import show_permid, show_permid_short
from Tribler.Core.BuddyCast.buddycast import BuddyCastFactory, BuddyCastCore
#from Tribler.Core.BuddyCast.buddycast import bin2str, str2bin, show_permid, show_permid_short
from Tribler.Core.SocialNetwork.RemoteQueryMsgHandler import RemoteQueryMsgHandler
from Tribler.Core.Utilities.utilities import get_collected_torrent_filename
from Tribler.Core.Statistics.Status.Status import get_status_holder
from Tribler.Core.Statistics.Status.FriendshipStats import FriendshipScore
from Tribler.Core.Statistics.Status.FriendshipStats import MAX_FRI
