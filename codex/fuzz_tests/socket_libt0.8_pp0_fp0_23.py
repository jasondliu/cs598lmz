import socket
import select
import os
import sys
import time
import json
from datetime import datetime
import threading

from conf import *
from server_utils import *

class Main(object):
    def __init__(self):
        self.statistics = Statistics()
        signal.signal(signal.SIGINT, self.clean_up)
        self.connections = {}

    def clean_up(self, signal, frame):
        print 'Stopping server'
        sys.exit(0)

    def update_statistics(self):
        while True:
            print '{} {} {} {}'.format(self.statistics.total_requests,
                                       self.statistics.total_successful_requests,
                                       self.statistics.slowest_request,
                                       self.statistics.fastest_request)
            self.statistics.update()
            time.sleep(STATISTICS_INTERVAL_IN_SECONDS)

    def update_connections(self, connection):
        self.connections[connection.fileno()] = connection


