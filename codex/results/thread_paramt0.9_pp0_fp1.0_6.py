import sys, threading
threading.Thread(target=lambda:  sys.stdout.write('\n')).start()
import time
import socket
import string
from urllib import request as urllib_request
import uuid
import http.client
import urllib
import json
import random
import os

sys.path.append('..')
os.chdir('..')

import shared_handles as sh

### This is the information required to make the bot talk to the web services
### server and send it data relevant to the experiment.

logger = sh.Logger()
statusreplacer = sh.StatusReplacer()

class Bot(object):
    """
    Abstract class for passing certain messages to another entity.
    """

    def __init__(self):
        pass

    def _update_status(self, text, *args, **kwargs):
        """
        Passes from one class to the next so that the main (web server)
        thread knows that certain messages have been sent.
        """
        pass

    def send_poll_message(self, text, *args, **kwargs):
        """
       
