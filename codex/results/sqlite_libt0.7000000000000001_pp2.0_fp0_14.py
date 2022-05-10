import ctypes
import ctypes.util
import threading
import sqlite3

# import libxml2
import lxml.etree as etree

import libmproxy.console.contentview as contentview
import libmproxy.console.palettes as palettes

import controller
import utils
import version
import dirtyvty
import flowfilter


DNS_REFRESH = 60

Intercept = controller.InterceptMaster

class StatusBar:
    def __init__(self, master):
        self.master = master
        self.v = urwid.Text([""])
        self.v_locked = urwid.Text([""])
        self.v_intercept = urwid.Text([""])
        self.v_limit = urwid.Text([""])
        self.v_filter = urwid.Text([""])
        self.v_connection = urwid.Text([""])

    def content(self):
        if self.master.options.intercept:
            i = urwid.AttrMap(self.v_intercept, "header")
        else:
            i = urwid.Text
