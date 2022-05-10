import ctypes
import ctypes.util
import threading
import sqlite3

# from scipy.io import wavfile
# from scipy.signal import resample
import sounddevice as sd
import soundfile as sf
from pygame import mixer
from pydub import AudioSegment

# Import library parts
from . import Audio, util
from .db import AudioTable


class SoundDeviceError(Exception):
    """Exceptions during SoundDevice usage"""
    pass


class GenericSoundDevice(Audio):
    """Superclass for audio devices using the sounddevice library

    """

    def __init__(self, *args, **kwargs):
        Audio.__init__(self, *args, **kwargs)
        self._initialized = False

    def init(self):
        if self._initialized:
            return True
        try:
            self.set_device()
        except sd.PortAudioError:
            self._log.warning("PortAudio or sounddevice could not be "
                              "initialized. It may not be installed.")
            return False
        except Exception as err:
            self._log.warning("Could not initialize audio device: {}".
