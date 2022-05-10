import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import os
import time
import math
import numpy as np
import pya3rt
import MeCab
import tkinter
import tkinter.font
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from gtts import gTTS
from playsound import playsound
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('-word', default=None)
args = parser.parse_args()
# MeCab setting
m = MeCab.Tagger("-Owakati")

# Hatena API Key
hatena_api_key = "hatena API key"
# A3rt API Key
# takk API Key
takk_api_key = "a3rt API key"
# Google API Key

# Speech API Key
speech_api_key = "tts API key"

# Voice Setting
voice_code = "Hikari"

# 定数(Do not change)
SP
