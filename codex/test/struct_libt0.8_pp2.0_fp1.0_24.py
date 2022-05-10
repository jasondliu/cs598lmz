import _struct
import array
import fcntl
import termios
import select
import signal
import subprocess
import os
import time
import re
import optparse
import pdb

import term.terminfo as terminfo
import term.termcap as termcap

import emu

class Terminal(object):
    def __init__(self,term="default"):
        self.name=term
        self.is_a_terminal = self.find_terminal_capability()

        self.request_tuple = None
        
    def find_terminal_capability(self):
        try:
            self.terminal_info = terminfo.Terminfo(self.name)
        except terminfo.TerminfoError:
            try:
                self.terminal_info = termcap.Termcap(self.name)
            except termcap.TermcapError:
                raise term.UnsupportedTerminalError("No terminal database found")

        self.tigetstr = self.terminal_info.tigetstr
        self.tigetnum = self.terminal_info
