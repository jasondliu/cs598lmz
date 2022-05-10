from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, length=0: b''  # shutup about not flushing

import os, sys, time
import urllib.request
import random, string
import logging, logging.config

from . import Object
import .Utils

class Database:
    '''Represents a database that stores objects.

    :param str path: path to the database directory (for saving tokens)
    :param str host: the hostname where the database lives
    :param int port: port number for database address
    :param str database: database name
    :param bool verbose: If True, connection and requests will be logged to stdout
    :param bool insecure: if True, all SSL certificates will be trusted
    :param bool compress: if True, send/receive compressed data
    :param bool version: version of the database protocol to use
        (only 2 is supported currently)
    :param str auth_token: authentication token to use
    :param str region: region identifier for database
    :param int timeout: socket timeout in seconds
    :param int max_retries: number of times a request should be retried
