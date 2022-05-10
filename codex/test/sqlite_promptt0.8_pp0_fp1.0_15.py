import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    conn = sqlite3.connect('test.db')
except:
    print("SQLite3 cannot connect!")
    exit()

cursor = conn.cursor()
# set global constants

MAX_FLOAT = 999999999.99

COL_NAME_LEN = 12

CUSTOMER_TABLE = "customer"
ORDER_TABLE = "order_table"
ITEM_TABLE = "item"

ERR_CODE_UNKNOWN = 0
ERR_CODE_SUCCESS = 1
ERR_CODE_DUPLICATE_CUSTOMER = 9001
ERR_CODE_DUPLICATE_ORDER = 9002
ERR_CODE_DUPLICATE_ITEM = 9003

NULL = None

# set global variables

global_lock = threading.Lock()

customer_lock = threading.Lock()

order_lock = threading.Lock()

item_lock = threading.Lock()

# set datastructures

