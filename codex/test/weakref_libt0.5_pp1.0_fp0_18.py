import weakref
import logging

from twisted.internet import defer

import p2pool
from p2pool.util import deferral, jsonrpc

logger = logging.getLogger('p2pool')

@deferral.retry('Error while checking bitcoind connection:', 1)
@defer.inlineCallbacks
def check(bitcoind, net):
    if not (yield net.PARENT.RPC_CHECK(bitcoind)):
        raise deferral.RetrySilentlyException()
    if not net.VERSION_CHECK((yield bitcoind.rpc_getinfo())['version']):
        raise Exception('bitcoind version unsupported')

def get_subsidy(bitcoind, target):
    return bitcoind.rpc_getblock(target)['coinbasevalue']

def get_xcoin_work(bitcoind, block_hash, share_target):
    return defer.succeed(bitcoind.rpc_getblock(block_hash)['bits'])
