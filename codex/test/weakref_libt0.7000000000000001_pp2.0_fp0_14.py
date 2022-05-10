import weakref, os, sys, logging
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from idlelib import macosx
from idlelib.configHandler import idleConf
from idlelib.configSectionNameDialog import SectionNameDialog
from idlelib import configDialog

# The following is a hack to force IDLE to load tkinter.tix, otherwise
# the tabs between the notebooks in the config dialog won't work.
try:
    from idlelib import tix
except:
    pass

class ConfigDialog(configDialog.ConfigDialog):

    def __init__(self, parent, title, _htest=False, _utest=False):
        configDialog.ConfigDialog.__init__(self, parent, title)
        self.htest = _htest
        self.utest = _utest
        self.create_widgets()
        self.apply_buttons_state()
        if self.htest:
            self.load_from_configuration()
        else:
            self.load_from_idleConf
