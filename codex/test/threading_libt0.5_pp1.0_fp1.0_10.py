import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
from pygame import mixer
from pygame.mixer import Sound
from pygame.mixer import music
import random
import time
import cv2
import numpy as np
import os
from pydub import AudioSegment
from pydub.playback import play

from multiprocessing import Process, Queue, Pool

import speech_recognition as sr
#from pydub.utils import mediainfo
from pydub import AudioSegment
from pydub.playback import play

def convert_mp3_to_wav(mp3_file):
    # read in mp3 file
    audio_file = AudioSegment.from_mp3(mp3_file)
    # export to wav
    filename = mp3_file.split(".")[0]
    audio_file.export(filename+".wav", format="wav")
    print("Done converting to wav")

def play_audio(mp3_file):
    audio_file = Audio
