import ctypes
import ctypes.util
import threading
import sqlite3

import qt.gui.style

import wayround_i2p.utils.path
import wayround_i2p.utils.file


import wayround_i2p.aipsetup.interact

import wayround_i2p.aipsetup.modules.compiled.info


class Help:

    def __init__(self):
        pass

    def __call__(self, controlling_obj):
        print(
            """
    Help text here
            """
            )
        return 0


class Run:

    def __init__(self):
        pass

    def __call__(self, controlling_obj):

        ctl = controlling_obj

        # FIXME: implement

        return 0


class RunGUI:

    def __init__(self):
        pass

    def __call__(self, controlling_obj):

        ctl = controlling_obj

        ctl.set_title('AiPSuite: Index')

        #print(repr(qt.gui.style.QStyleFactory.keys()))

        app = c
