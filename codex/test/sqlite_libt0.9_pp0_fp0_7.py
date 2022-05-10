import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import sys

if sys.version_info[0] == 2:
    import Queue as queue
else:
    import queue


sqlite3.enable_callback_tracebacks(True)


librtmidi_dllpath = ctypes.util.find_library('librtmidi')
if not librtmidi_dllpath:
    # TODO: !!! raise an error
    raise ImportError('librtmidi not found')
librtmidi = ctypes.cdll.LoadLibrary(librtmidi_dllpath)


class RtInstrument(object):
    '''
    Create and handle an RtMidiIn object.
    
    If a callback is provided, it will be called when MIDI messages come in.
    It should take two arguments:  timestamps and messages
    
    Otherwise, MIDI messages will go into a queue and can be retrieved with
    self.get_message()
    '''
    def __init__(self, devicename, callback=None):
        self.instrument = c
