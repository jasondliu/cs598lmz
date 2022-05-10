import sys, threading
threading.Thread(target=lambda: sys.stdout.write("")).start()

def flush_stdout_intermediate():
    print("", flush=True)

flush_stdout_intermediate()

import datetime
import os
import time
import traceback
import types

def flush_stdout():
    print("", flush=True)

def flush_stderr():
    print("", flush=True, file=sys.stderr)

def node_manager_log_debug(msg):
    print("DEBUG: " + msg, flush=True, file=sys.stderr)

def node_manager_log_info(msg):
    print("INFO: " + msg, flush=True, file=sys.stderr)

def node_manager_log_warning(msg):
    print("WARNING: " + msg, flush=True, file=sys.stderr)

def node_manager_log_error(msg):
    print("ERROR: " + msg, flush=True, file=sys.stderr)

def timedelta_total_seconds(timedelta
