import socket
import sys
import logging
import threading
import time
import argparse
import configparser
import struct
import libvirt
import os,glob
class Timeout(object):

    def __init__(self, seconds, error_message='Timeout'):
	    self.seconds = seconds
	    self.error_message = error_message
	
    def handle_timeout(self, signum, frame):
	    raise TimeoutError(self.error_message)
	
    def __enter__(self):
	    signal.signal(signal.SIGALRM, self.handle_timeout)
	    signal.alarm(self.seconds)
	
    def __exit__(self, type, value, traceback):
	    signal.alarm(0)

class LocalPresenter(object):
    def __init__(self, mainConfig):
        self.mainConfig = mainConfig
        self.presenterName = mainConfig["presenterName"]
        self.master = mainConfig["master"]
        
        self.localTime = 0
        self.errorFlag =
