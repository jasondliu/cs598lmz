import _struct
import struct
import sys
import time

from _Framework import Task
from Launchpad import Launchpad

__version__ = '0.2.0'

class MonoRouter(Launchpad):

    def receive_midi(self, port_no, midi_bytes):
        mono_out = self._mono_out
        midi_bytes = list(midi_bytes)
        if midi_bytes[0] & 240 == 192:
            self._send_midi(mono_out, midi_bytes)
            return
        if self._is_enabled:
            if self._mode == 0:
                if midi_bytes[0] & 240 == 128:
                    return
                if self._last_note != midi_bytes[1]:
                    if self._last_note != -1:
                        self._send_midi(mono_out, [128, self._last_note, 0])
                    self._last_note = midi_bytes[1]
                    self._send_midi(mono_out, midi_bytes)
                return
