import ctypes
import ctypes.util
import threading
import sqlite3
import os
import signal
import time
import re
import subprocess
import sys
import signal
import datetime
import pprint
import socket

# This is how we get the system's network interface names.
import netifaces

"""
This is the main class that we use to get all the information we need.
"""
class Iperf():
    def __init__(self):
        self.iperf_path = "iperf"

    def run_iperf(self, host, port, mode, time, extra_params):
        """
        Run the iperf client and return the output.

        Arguments:
        host -- the hostname or IP address of the server
        port -- the port number to bind to
        mode -- the mode to run in: client or server
        time -- the length of time to run the test for
        extra_params -- extra parameters to pass to the iperf client
        """
        iperf_args = [self.iperf_path, "-c", host, "-p", str(port), "-t", str(time), "-y", "c"]
