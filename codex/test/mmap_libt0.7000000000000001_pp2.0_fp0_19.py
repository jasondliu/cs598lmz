import mmap
import signal
import sys
import time
import os
import socket
import threading

from datetime import datetime
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM

import RPi.GPIO as GPIO
from PIL import Image

# global variables
image_name = "image.jpg"
