import socket
import sys
import time
import random
import threading
import os
import datetime
import logging

#logging.basicConfig(level=logging.DEBUG,
#                    format='(%(threadName)-10s) %(message)s',
#                    )

#logging.basicConfig(filename='log.txt', level=logging.DEBUG,
#                    format='(%(threadName)-10s) %(message)s',
#                    )

class ThreadClass(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return


# Create two threads as follows
for i
