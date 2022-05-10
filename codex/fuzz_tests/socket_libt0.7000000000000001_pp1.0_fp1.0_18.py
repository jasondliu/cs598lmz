import socket
import time
import json
from common import config
from client import Client
import logging
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys
import datetime
from subprocess import Popen, PIPE, STDOUT

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

    file_handler = logging.FileHandler('client.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


class Client(Client):
    '''
        This class is an implementation of the Client class from the common package.
        It is meant to be used by a node that is only a client.
    '''
    def __init__(self, name, config_path='common/config.json'):
        '''
            name
