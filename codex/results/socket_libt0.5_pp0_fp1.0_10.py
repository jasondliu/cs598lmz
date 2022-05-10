import socket
import sys
import time
import threading
import numpy as np
import cv2
import signal
import os

#Define the IP address of the server
#IP_ADDR = '192.168.1.102'
IP_ADDR = '192.168.43.90'
#Define the port number of the server
PORT = 1337
#Define the size of the packet to be sent
PACKET_SIZE = 1024
#Define the number of packets to be sent
NUM_PACKETS = 1
#Define the number of bytes per packet
BYTES_PER_PACKET = PACKET_SIZE * NUM_PACKETS
#Define the number of bytes per frame
BYTES_PER_FRAME = BYTES_PER_PACKET * 20
#Define the number of bytes per image
BYTES_PER_IMAGE = BYTES_PER_FRAME * 3
#Define the number of bytes per second
BYTES_PER_SECOND = BYTES_PER_IMAGE * 20

#Define the number of bytes per
