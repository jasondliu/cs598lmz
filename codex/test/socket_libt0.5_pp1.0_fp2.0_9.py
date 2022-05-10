import socket
import sys
import time
import threading
import signal
import json
import random
import os
import math
import re
import subprocess

from datetime import datetime

from pydub import AudioSegment
from pydub.playback import play

import pyaudio
import wave

from colorama import init, Fore, Back, Style
init(convert=True)

import urllib.request

# https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python
def play_sound(file):
    chunk = 1024  # split our sound file up into chunks
    wf = wave.open(file, 'rb')  # open the sound file
    pa = pyaudio.PyAudio()  # instantiate the pyAudio class

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

