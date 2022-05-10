import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

class _PulseAudio:
    def __init__(self):
        self.pa_mainloop = None
        self.pa_mainloop_api = None
        self.pa_context = None
        self.pa_op = None
        self.pa_state = None
        self.pa_proplist = None
        self.pa_proplist_p = None
        self.pa_proplist_c = None
        self.pa_proplist_c_p = None
        self.pa_proplist_c_p_p = None
        self.pa_proplist_c_p_p_p = None
        self.pa_proplist_c_p_p_p_p = None
        self.pa_proplist_c_p_p_p_p_p = None
        self.pa_proplist_c_p_p_p_p_p_p = None
        self.pa_proplist_c_p_p_p_p_p_p_p = None
