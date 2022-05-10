import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import threading
import subprocess

from . import config
from . import util
from . import log

def start_server(config):
    if config.get('server_port') is None:
        return
    if config.get('server') is None:
        return

    cmd = '{} -p {} -b {} -P {}'.format(
        config['server'],
        config['server_port'],
        config['server_bind'],
        config['server_password'],
    )

    log.info('Starting server')
    log.debug('cmd: {}'.format(cmd))
    util.run_cmd(cmd, cwd=config['root'])

def start_client(config):
    if config.get('client_port') is None:
        return
    if config.get('client') is None:
        return

    cmd = '{} -p {} -b {} -P {}'.format(
        config['client'],
        config['client_
