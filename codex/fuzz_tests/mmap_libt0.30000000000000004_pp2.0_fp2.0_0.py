import mmap
import os
import re
import sys
import time

from datetime import datetime
from optparse import OptionParser
from subprocess import Popen, PIPE

from pymongo import Connection
from pymongo.errors import ConnectionFailure

from mongo_connect import mongo_connect

def main():
    usage = """usage: %prog [options]
    """
    parser = OptionParser(usage=usage)
    parser.add_option("--host", dest="host", default="localhost",
                      help="mongodb host to connect to")
    parser.add_option("--port", dest="port", default=27017, type="int",
                      help="mongodb port to connect to")
    parser.add_option("--db", dest="db", default="test",
                      help="database to use")
    parser.add_option("--collection", dest="collection", default="test",
                      help="collection to use")
    parser.add_option("--username", dest="username", default=None,
                      help="username for authentication")
    parser.add_option
