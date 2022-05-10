import ctypes
import ctypes.util
import threading
import sqlite3

import os
import sys
import time
import socket
import subprocess
import re
import json
import shutil
import signal
import traceback
import platform

import util
import config
import web
import database
import heartbeat
import log
import disk
import user
import backup
import restore
import remote
import share
import hash
import i18n
import jsonrpc
import update
import acl

class Server:
	def __init__(self, options, args):
		self.options = options
		self.args = args
		self.config = config.Config()
		self.data_dir = 'data'
		self.sock_path = 'sock'
		self.pid_path = 'pid'
		self.log_path = 'log'
		self.backup_path = 'backup'
		self.share_path = 'share'
		self.temp_path = 'temp'
		self.share_dir = 'share'
		self.web_dir = 'web'
		self
