import types
types.ModuleType.__getitem__ = lambda self, x: getattr(self, x)

import socket

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.bind(('<broadcast>', 9999))

logger.info('Listening for announcements...')

announcements = {}
tasks = []

def task(function):
    tasks.append(function)
    return function

def lookup_announcement(data):
    return announcements[data]

@task
def invite():
    while True:
        data, address = server.recvfrom(1024)
        logger.info('Received announcement from `{0}` at `{1}`'.format(*address))
        if data in announcements:
            raise NameError('Announcement for `{0
