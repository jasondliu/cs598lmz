import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import cPickle as pickle
import utils

class Process(object):
	_processes = {}
	_processes_lock = threading.Lock()

	@classmethod
	def get_process_by_pid(cls, pid):
		pid = int(pid)
		with cls._processes_lock:
			if pid not in cls._processes:
				cls._processes[pid] = cls(pid)
			return cls._processes[pid]

	@classmethod
	def get_current_process(cls):
		return cls.get_process_by_pid(os.getpid())

	def __init__(self, pid):
		self.pid = pid
		self.ppid = None
		self.uid = None
		self.comm = None
		self.exe = None
		self._stat = None
		self._statm = None
		self.envp = {}
		self.get_
