import socket
import sys
import os
import threading
import time
import queue
import struct
import random
import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import subprocess
import wave
from datetime import datetime
from scipy.fftpack import fft
from scipy.signal import butter, lfilter
from scipy.signal import freqz
import cv2
from PIL import Image
import pyaudio
import wave
import timeit
from time import sleep

# Global variables
# socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 7))

# sensor
sensor_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
