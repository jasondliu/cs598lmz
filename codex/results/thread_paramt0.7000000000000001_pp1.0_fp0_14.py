import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

import pyaudio
import wave
import time
import math
import numpy as np
import os, sys
import base64
import json

from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus

# 音声ファイルの読み込み
def read_wave(filename):
    wf = wave.open(filename, "r")
    fs = wf.getframerate()
    x = wf.readframes(wf.getnframes())
    x = np.frombuffer(x, "int16") / 32768.0  # -1 - +1に正規化
    wf.close()
    return x, float(fs)


def play(stream, chunk, fs=44100):
    t = 1.0 / fs # 1サンプルの長さ(秒
