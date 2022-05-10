import gc, weakref, sys, types, traceback, inspect, re, io, os, io
import _thread, threading, signal, linecache

import json

class Printable:
    """
    Base class for all printable objects (i.e., objects that are visible in the
    debugger).
    """

    def __str__(self):
        return str(vars(self))

# Printable classes

class Thread(Printable):
    """
    Thread information class.
    """

    def __init__(self, thread):
        self.id = thread.ident
        self.name = thread.name

class Frame(Printable):
    """
    Frame information class.
    """

    def __init__(self, frame, f_globals=None, f_locals=None):
        globalInFrame = False
        if f_globals is None:
            globalInFrame = True
            f_globals = frame.f_globals
            f_locals = frame.f_locals
        self.f_lineno = frame.f_
