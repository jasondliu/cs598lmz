import socket
import time
import sys
import select
import threading
import random
import re
import os
import signal
import argparse
from threading import Thread
from thread import *
from random import choice

#---------------------------------------------------------------------------------

def log(text):
    print "["+str(time.strftime("%H:%M:%S"))+"] "+text

def log_debug(text):
    if config["debug"]:
        log("[DEBUG] " + text)

def log_error(text):
    log("[ERROR] " + text)

def log_info(text):
    log("[INFO] " + text)

def log_warning(text):
    log("[WARNING] " + text)

def log_server(text):
    log("[SERVER] " + text)

def log_client(text):
    log("[CLIENT] " + text)

def log_chat(text):
    log("[CHAT] " + text)

def log_command(text):
    log("[COMMAND] " + text
