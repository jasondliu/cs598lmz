import codecs
# Test codecs.register_error('ignore', codecs.ignore_errors)

import sys
import os
import re
import time
import datetime
import optparse
import subprocess
import shutil

import xml.etree.ElementTree

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

# Gst.init(None)

import pygst
pygst.require("0.10")
import gst

import numpy
import numpy.fft

import scipy
import scipy.fftpack

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pyaudio

import wave

import scipy.io.wavfile

import scipy.signal

import scipy.misc

import pygame

import pygame.sndarray

import pygame.mixer

import pygame.mixer.music

import Image

import ImageChops

import random

import math

