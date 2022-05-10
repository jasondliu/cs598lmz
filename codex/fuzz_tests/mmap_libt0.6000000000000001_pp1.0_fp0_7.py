import mmap
import struct
import os

from collections import defaultdict

from dmoj.error import InternalError
from dmoj.utils.unicode import utf8text
from dmoj.utils.ansi import ansi_style


class ExecutableResult(object):
    def __init__(self):
        self.time = 0
        self.memory = 0
        self.output = ''
        self.result = ''
        self.signal = 0
        self.returncode = 0
        self.re_flag = False
        self.re_data = ''

    def __str__(self):
        return '%d %d %d %d %s' % (self.time, self.memory, self.signal,
                                   self.returncode, self.result)

    def set(self, time, memory, signal, returncode, result):
        self.time = time
        self.memory = memory
        self.signal = signal
        self.returncode = returncode
        self.result = result

    def set_re(self, data):
        self
