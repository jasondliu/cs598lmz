import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui

import rtmidi
try:
    m = rtmidi.MidiIn()
    m.get_ports()
    del m
    QT_USE_PYMIDI = True
except rtmidi.RtMidiError as e:
    QT_USE_PYMIDI = False

DEFAULT_MIXER_FILENAMETEMPLATE = 'IO_POPUP_{port}_{channel}_{title}.mix'

def tuplist2dic(l, value=None):
    if l:
        g = groupby(l, lambda x:x[0])
        return {k:list(map(itemgetter(1), gg)) for k, gg in g}
    else:
        return {}

