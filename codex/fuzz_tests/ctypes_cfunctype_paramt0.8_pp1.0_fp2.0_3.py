import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int, ctypes.c_void_p)

import sys
PY2 = sys.version_info[0] == 2

import os

if PY2:
    def _intlike(s):
        return s if isinstance(s,int) else ord(s)
else:
    def _intlike(s):
        return s

def null_callback(param1, param2):
    pass

class MIDIDevice(object):
    def __init__(self, device, is_input=False):
        self.name = device.contents.name
        self.uid  = device.contents.uid

        self._device = device
        self._is_input = is_input

    def open(self):
        self._stream = libmidi.MIDIStreamOpen(
            self._device,
            FUNTYPE(null_callback),
            None)

        if self._stream is None:
            raise MIDIError(None)

        self._stream = self._stream[0]

    def
