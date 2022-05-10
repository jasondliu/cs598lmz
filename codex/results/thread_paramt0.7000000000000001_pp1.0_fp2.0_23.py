import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

from pythonosc.osc_message_builder import OscMessageBuilder

from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import make_chunks
import time
from pynput.mouse import Button, Controller
mouse = Controller()
import cv2

import numpy as np
from PIL import Image
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class Loop:

