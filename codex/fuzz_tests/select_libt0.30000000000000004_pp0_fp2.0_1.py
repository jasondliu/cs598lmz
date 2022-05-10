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
from pymongo.mongo_replica_set_client import MongoReplicaSetClient
from pymongo.read_preferences import ReadPreference
from test import (client_context,
                  client_knobs,
                  client_knobs_opts,
                  client_knobs_opts_threaded,
                  client_knobs_opts_threaded_write_concern,
                  client_knobs_opts_threaded_write_concern_no_gle,
                  client_knobs_opts_threaded_write_concern_no_gle_no_ack,
                  client_knobs_opts_threaded_write_con
