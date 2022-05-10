import threading
# Test threading daemon
import time
import os
import sys

import logging
logging.basicConfig(filename='/tmp/error.log',level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

# This is the daemon module
import daemon

# Import the script that needs to be run in the background
import controller

# This is the script that will be run in the background
script_name = 'controller.py'

# Define a new class that will be used to create the daemon
class MyDaemon(daemon.Daemon):
    def run(self):
        while True:
            # Run your script here
            execfile(script_name)
            time.sleep(1)

if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop
