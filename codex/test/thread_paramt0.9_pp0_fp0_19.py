import sys, threading
threading.Thread(target=lambda:reactor.run(installSignalHandlers=0)).start()
sys.dont_write_bytecode=True

import os
from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Gobject
from gi.repository import Notify
GObject.threads_init()
Gtk.init(sys.argv)
Notify.init("app")

### helper functions ###

class ArgumentParser(object):
    def __init__(self, **options):
        self.__dict__.update(options)
        self.__dict__['__set'] = True
        if self.parser is None:
            self.parser = ArgumentParser.Parser(prog=self.prog,usage=self.usage)
        self.parser.__dict__.update(self.__dict__)
    def __msg(self, msg, msgtype):
        if self.msgtype == msgtype:
            print(msg, end="")
