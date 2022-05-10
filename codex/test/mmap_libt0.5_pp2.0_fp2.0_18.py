import mmap
import os
import re
import subprocess
import sys
import time
import traceback

from collections import OrderedDict

import numpy as np

from evdev import InputDevice, categorize, ecodes

from PIL import Image, ImageDraw, ImageFont

from bme280 import BME280

from ltr559 import LTR559

from rgbmatrix import RGBMatrix, RGBMatrixOptions

from smbus2 import SMBus

import RPi.GPIO as GPIO

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
from aiy.voice.audio import AudioFormat, play_wav, record_file, Recorder

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

from gpiozero import Button

from signal import pause

# Initialize the GPIO Pins
GPIO.setmode(GPIO.BCM)

