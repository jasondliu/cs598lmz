import select
import sys
import os
import time
import pyudev

from fcntl import fcntl
from fcntl import F_GETFL
from fcntl import F_SETFL
from os import O_NONBLOCK

DEV = "/dev/ttyACM0"

def test():
	print("test")


def read_serial_line(port):
	try:
		ret = port.readline()
		return ret
	except:
		return None
	

def set_blocking(fd, blocking):
	flags = fcntl(fd, F_GETFL)
	if not blocking:
		flags |= O_NONBLOCK
	else:
		flags &= ~O_NONBLOCK
	fcntl(fd, F_SETFL, flags)


def main():

	context = pyudev.Context()
	monitor = pyudev.Monitor.from_netlink(context)
	monitor.filter_by(subsystem='tty')
	observer = pyudev.MonitorObs
