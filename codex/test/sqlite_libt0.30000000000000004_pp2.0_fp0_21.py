import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import traceback
import urllib
import urllib2
import json

#
# Global variables
#

# The path to the sqlite database file
db_path = None

# The path to the file containing the last known block number
block_number_path = None

# The path to the file containing the last known block hash
block_hash_path = None

# The path to the file containing the last known block time
block_time_path = None

# The path to the file containing the last known block difficulty
block_difficulty_path = None

# The path to the file containing the last known block merkle root
block_merkle_root_path = None

# The path to the file containing the last known block nonce
block_nonce_path = None

# The path to the file containing the last known block version
block_version_path = None

# The path to the file containing the last known block transaction count
block_transaction_count_path = None

