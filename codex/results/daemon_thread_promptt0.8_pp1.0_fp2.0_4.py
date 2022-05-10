import threading
# Test threading daemon
import time
import random

# For debug
import sys

# For test
# Import the email modules we'll need
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Import the email modules we'll need

import email.mime.multipart
import email.mime.text

import email.mime.base
import mimetypes

import os.path


# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def get_source_files():
    # Get list of source files
    # If a file is not exist, retry to get it again
    list_file_names = ['file1.txt','file2.txt','file3.txt']
    while(True):
        try:
            # Do something
            print("Downloading files")
            time.sleep(random.randint(1,5))
            return list_file_names
        except:
            # Do something else when error happens
            print("Downloading
