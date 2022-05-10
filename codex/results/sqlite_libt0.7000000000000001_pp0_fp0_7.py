import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import rtmidi_python as rtmidi
import time
import sys
import os
import signal

PY_MAJOR_VER = sys.version_info[0]

if PY_MAJOR_VER == 2:
    from Queue import Queue
    from Queue import Empty
    from Queue import Full
    from urlparse import urlparse
elif PY_MAJOR_VER == 3:
    from queue import Queue
    from queue import Empty
    from queue import Full
    from urllib.parse import urlparse
else:
    print("Unsupported Python version %d.%d" % (
        sys.version_info[0], sys.version_info[1]))
    sys.exit(1)


def get_midi_ports():
    """Return a list of (name, is_input, idx) tuples describing each
    MIDI port available on the system."""
    midiin = rtmidi.MidiIn()
    midiout = rtmidi.MidiOut()

   
