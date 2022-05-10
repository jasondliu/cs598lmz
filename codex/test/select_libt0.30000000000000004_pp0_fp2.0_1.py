import select
import socket
import sys
import threading
import time

import pytest

import pymongo
from pymongo import common
from pymongo.errors import (AutoReconnect,
                            ConfigurationError,
                            ConnectionFailure,
                            DocumentTooLarge,
                            InvalidOperation,
                            OperationFailure,
                            WTimeoutError)
from pymongo.mongo_client import MongoClient
