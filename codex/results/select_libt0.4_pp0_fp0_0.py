import select
import sys
import time
import traceback

from . import config
from . import log
from . import utils
from . import version
from . import watcher
from . import web
from . import xdg

logger = log.get_logger()


def main():
    config.load()
    if config.args.daemon:
        daemonize()
    if config.args.log_level:
        log.set_level(config.args.log_level)
    log.set_file(config.args.log_file)
    logger.info('Starting %s %s', version.NAME, version.VERSION)
    logger.debug('Using config file %s', config.config_file)
    if config.args.debug:
        logger.debug('Debug mode enabled')
    if config.args.web_debug:
        logger.debug('Web debug mode enabled')
    if config.args.web_port:
        logger.debug('Web port set to %s', config.args.web_port)
    watcher.start()
    web.start()
