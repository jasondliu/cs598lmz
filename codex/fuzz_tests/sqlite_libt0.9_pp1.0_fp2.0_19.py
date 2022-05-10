import ctypes
import ctypes.util
import threading
import sqlite3
import logging
from datetime import datetime

DEVICE_STATUS_LENGTH = 32

DEVICE_STATUS = [
        (0, "device is the preferred playback device"),
        (1, "device is the default communication device"),
        (2, "the Win32 waveIn APIs are enabled"),
        (3, "device supports volume control"),
        (4, "device supports left-right volume control"),
        (5, "device supports pitch control"),
        (6, "device supports playback rate control"),
        (7, "device supports voice control"),
    ]

DEVICE_FORMATS = [
        (0, "Not Specified"),
        (1, "Integer PCM"),
        (2, "Floating Point PCM"),
        (3, "Extensible"),
        (4, "MuLaw"),
        (5, "ALaw"),
        (6, "ADPCM"),
        (7, "Ima ADPCM"),
        (8, "DSP Group TrueSpeech"),
        (9, "Microsoft GSM"),
        (10, "MP3
