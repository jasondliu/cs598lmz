import mmap
from argparse import ArgumentParser
from subprocess import Popen, PIPE

class Log([object]):
    def __init__(self, path, pidfile):
        try:
            self.pidfile = open(pidfile, 'r+')
            self.pid = int(self.pidfile.read())
            self.pidfile.close()
        except IOError:
            open(pidfile, 'w').close()
            print 'Cannot read pidfile. Switching to normal mode'
            self.pid = None
        self.path = path
        self.logfile = None
        self.mm = None

    def log_and_seek(self, line, skip=False):
        if not self.logfile:
            self.logfile = open(self.path, 'a')
        self.logfile.write('%s\n' % line)
        if skip:
            self.logfile.seek(self.mm.tell())

    def seek(self):
        if self.logfile:
            self.mm.seek(self.logfile.tell
