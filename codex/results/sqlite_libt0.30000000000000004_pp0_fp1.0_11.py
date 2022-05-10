import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import subprocess
import signal
import logging
import logging.handlers

# Global variables
#
# The following variables are used by the main thread and the
# signal handler thread.
#
#   g_logger - The logger object
#   g_db - The database connection
#   g_db_lock - The lock for the database connection
#   g_running - Whether the program is running
#   g_signal_handler_thread - The thread that handles signals
#   g_signal_handler_thread_lock - The lock for the signal handler thread
#
# The following variables are used by the main thread and the
# worker threads.
#
#   g_worker_threads - The list of worker threads
#   g_worker_threads_lock - The lock for the list of worker threads
#   g_worker_threads_cond - The condition variable for the list of worker
#                           threads
#   g_worker_threads_num - The number of worker threads
#   g_worker_threads_num_lock - The lock for
