import ctypes
import ctypes.util
import threading
import sqlite3
import string
import time
import posixpath
from os import listdir
from ConfigParser import ConfigParser
from struct import pack, unpack
from sshclient import SshCom


class SshDeviceFun(SshCom):
	def __init__(self, ssh_addr="localhost:22", ssh_user="root", ssh_pass=""):
		SshCom.__init__(self, ssh_addr, ssh_user, ssh_pass)
		self.addr = ssh_addr
		self.user = ssh_user
		self.passwd = ssh_pass
		self.connect_ssh()
		
	def get_test_case_list(self):
		cmd = "ls /usr/share/tina/current | grep .py"
		out = self.run_cmd(cmd).stdout.read()
		out = out.split("\n")
		return out
	def run_autotest(self, case_filename, runflag=0):
		if "." in case_filename:
			case_file
