import select
import socket
import sys
import time
import os
import threading
import signal
import subprocess
import logging

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# TODO:
# - make all code threadsafe
# - make code more robust

# TODO:
# - add a command to check if a file is open by a client
# - add a command to check if a client is connected
# - add a command to check if a client is connected to a file
# - add a command to check if a client is connected to a file with a given md5
# - add a command to check if a file is open by a client
# - add a command to check if a file is open by a client with a given md5
# - add a command to check if a client is connected to a file with a given md5
# - add a command to check if a client is connected to a file with a given md5
# - add a command to check if a file is open by a client with a given md5
# - add a command to check if a file is open by a
