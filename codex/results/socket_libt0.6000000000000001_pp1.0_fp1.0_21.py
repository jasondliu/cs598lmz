import socket
import sys
import threading
import time

import zmq

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from utils import db_utils
from utils import image_utils
from utils import text_utils

# Logging setup
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')
logger = logging.getLogger(__name__)

# Global variables
image_path = ''
image_name = 'image'
image_ext = '.jpg'

# Constants
DO_NOTHING = 0
LOAD_IMAGE = 1
GET_TEXT = 2
GET_TEXT_AND_SAVE = 3
GET_TEXT_AND_SAVE_AND_EXIT = 4
EXIT = 5

# Helper functions
def init_db():
    # Connect to MongoDB
    try:
        client = MongoClient
