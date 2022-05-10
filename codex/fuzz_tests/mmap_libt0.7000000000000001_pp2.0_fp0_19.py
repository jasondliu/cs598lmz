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
image_path = "/home/pi/images/"
image_path_and_name = image_path + image_name

# global constants
HOST = '127.0.0.1'
PORT = 5000

# Create a TCP/IP socket
sock = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the port
server_address = (HOST, PORT)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# global variable
global image_number


def image_capture(image_number):

    # create image name and image path
    image_
