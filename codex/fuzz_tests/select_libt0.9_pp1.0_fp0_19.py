import select
import sys
import json
import requests
import os

LOCK_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lock')
ERROR_MSG_SIZE = 4096


class SubProcessError(Exception):
    pass


class Proc(object):
    def __init__(self, cmd):
        self.lock()

        self.cmd = cmd

        self.master, self.slave = pty.openpty()
        self.process = subprocess.Popen(self.cmd, stdin=self.slave)
        self.w_pipe = os.fdopen(self.master, 'w+')
        self.r_pipe = os.fdopen(self.master, 'r+')

        self.pid = self.process.pid

    @staticmethod
    def lock():
        if os.path.exists(LOCK_PATH):
            raise Exception('Already locked: {}'.format(LOCK_PATH))
        open(LOCK_PATH, 'w+').close()

    @staticmethod
    def unlock():
       
