import select
import socket
import sys
import threading
import time

# Importing modules for image processing
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Importing modules for face detection and face recognition
import face_recognition
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# Importing modules for voice recognition
import speech_recognition as sr
from gtts import gTTS

# Importing modules for text to speech
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

# Importing modules for sending email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Importing modules for controlling mouse
from pynput.mouse import Button, Controller

# Importing modules for controlling keyboard
from pynput.keyboard import Key, Controller

# Import
