import threading
# Test threading daemon
import time
import json
import requests
import sys
import os
import traceback
import logging
import logging.handlers
import datetime

# Global variables
# Lock for threading
lock = threading.Lock()
# Variable for threading
threads = []
# Variable for threading
threads_stopped = False
# Variable for threading
threads_stopped_count = 0
# Variable for threading
threads_stopped_count_max = 0
# Variable for threading
threads_stopped_count_max_reached = False
# Variable for threading
threads_stopped_count_max_reached_time = None
# Variable for threading
threads_stopped_count_max_reached_time_delta = None
# Variable for threading
threads_stopped_count_max_reached_time_delta_max = None
# Variable for threading
threads_stopped_count_max_reached_time_delta_max_reached = False
# Variable for threading
threads_stopped_count_max_
