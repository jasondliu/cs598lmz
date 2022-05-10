import mmap
import subprocess
import multiprocessing
import select
from enum import Enum
import sys
import io
import os
from threading import Thread, Event
from time import sleep, time
import re


class Status(Enum):
    Idle = 0
    Running = 1
    Paused = 2
    Done = 3


class Process:
    def __init__(self, command, bufsize=0, bufsize_stdout=0, bufsize_stderr=0):
        self.command = command
        self.bufsize = bufsize
        self.bufsize_stdout = bufsize_stdout
        self.bufsize_stderr = bufsize_stderr
        self.retcode = -1
        self.is_stopped = False
        self.stdout = []
        self.stderr = []
        self.timestamp = []
        self.buffer_size = 0
        self.fd = []
        self.buffer_size_stdout = 0
        self.fd_stdout = []
