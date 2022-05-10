import weakref
import threading

from Tribler.Core.simpledefs import NTFY_DISPERSY, NTFY_TORRENTS, NTFY_PEERS, NTFY_MYPREFERENCES, NTFY_CHANNELCAST

from Tribler.community.channel.community import ChannelCommunity
from Tribler.community.channel.preview import PreviewChannelCommunity
from Tribler.dispersy.dispersy import Dispersy
from Tribler.dispersy.endpoint import StandaloneEndpoint
from Tribler.dispersy.util import blocking_call_on_reactor_thread
from Tribler.Core.SessionConfig import SessionStartupConfig
from Tribler.Core.CacheDB.SqliteCacheDBHandler import TorrentDBHandler, MyPreferenceDBHandler, PeerDBHandler, \
    VoteCastDBHandler, ChannelCastDBHandler
from Tribler.Core.Utilities.twisted_thread import deferred
from Tribler.Core.Utilities.twisted_thread import blockingCallFromThread


