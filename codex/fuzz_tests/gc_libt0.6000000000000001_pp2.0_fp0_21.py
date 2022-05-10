import gc, weakref, logging
from collections import defaultdict

from twisted.internet import reactor
from twisted.python import log
from twisted.internet.defer import Deferred, DeferredList
from twisted.python.failure import Failure

from p2pool import data as p2pool_data, p2p
from p2pool.bitcoin import data as bitcoin_data, p2p as bitcoin_p2p
from p2pool.util.deferral import retry, DeferredQueue, run_with_timeout
from p2pool.util import deferral, jsonrpc, math, variable

class Server(object):
    def __init__(self, wsgi_app, bitcoind_work, net, other_servers, bitcoind_p2p, bitcoind_rpc, datadir_path, get_share_hashes, share_pubkey_hash, share_pubkey, get_target_time, get_best_share_hash, get_best_share, get_target_block, get_max_target, get_nth_work, get_timer, get_desired_version
