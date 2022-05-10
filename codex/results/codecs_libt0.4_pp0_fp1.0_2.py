import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import AudioFileClip
from moviepy.video.fx.all import *

import os
import sys
import subprocess
import glob
import shutil
import time
import datetime
import re
import math

import moviepy.editor as mp

import threading

#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------

#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------

def youtube_downloader(url,path):

    try:
        global yt
        yt = YouTube(url)
    except:
        messagebox.showerror("Error","Invalid YouTube URL")
        return

    global title
   
