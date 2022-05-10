import gc, weakref, copy

import threading, logging

from mongoengine import connect
from mongoengine.connection import ConnectionError, disconnect

from docopt import docopt, DocoptExit

import pyzp.logger
log = logging.getLogger('pyzp')

import pyzp.config
from pyzp.config import config

import pyzp.core.peerdiscovery as peerdiscovery
import pyzp.core.peer as peer

import pyzp.core.net.server as server
import pyzp.core.net.client as client

log.info('starting pyzp daemon...')

# Start PeerDiscovery and ServiceDiscovery before main thread to set up necessary calls
peerdiscovery.start()

# Main thread starts
if __name__ == '__main__':
    ## Main Daemon
    log.info('initializing daemon...')

    ## Load from config
    config.pull()

    print(config.data)

    config.comment('test','works!','so much so','123','testing','success','lines','many','lines','.'
