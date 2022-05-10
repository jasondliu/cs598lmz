import ctypes
import ctypes.util
import threading
import sqlite3

from enum import Enum

libc = ctypes.CDLL(ctypes.util.find_library('c'))

_bpm_default = 120
_bpm_min = 60
_bpm_max = 240

_master_volume = 1.0

_pattern_max = 8

_fx_max = 2
_fx_size = 8

_step_size = 4
_step_max = 16

_voice_max = 12

_reverb_size = 8

_scale_size = 12

_scale_major = {
  'C': 0,
  'G': 1,
  'D': 2,
  'A': 3,
  'E': 4,
  'B': 5,
  'Gb': 6,
  'Db': 7,
  'Ab': 8,
  'Eb': 9,
  'Bb': 10,
  'F': 11
}

_scale_minor = {
  'Am': 0,
  'Em': 1,
  'Bm': 2,

