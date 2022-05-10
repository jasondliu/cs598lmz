import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time

#---------------------------------------------------------------------------------
#--------------------------------- GLOBALS ----------------------------------------
#---------------------------------------------------------------------------------

# Table of all the files that have been read
# file_name | [read/not read] | [locked/not locked] | [last read time]
# file_name is a string, and the other two are integers
FILE_TABLE_NAME = "file_table"
FILE_NAME_COLUMN = "file_name"
READ_COLUMN = "read"
LOCKED_COLUMN = "locked"
READ_TIME_COLUMN = "last_read_time"

# Table of all the processes that are currently running
# pid | [alive/not alive] | [locked/not locked] | [last updated time]
# pid is an integer, and the other two are integers
PROCESS_TABLE_NAME = "process_table"
PID_COLUMN = "pid"
ALIVE_COLUMN = "alive"
UPDATED_TIME_COLUMN = "last_updated_time"

# Table of all the files that have been
