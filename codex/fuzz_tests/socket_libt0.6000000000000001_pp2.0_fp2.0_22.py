import socket
import sys
import time

try:
    import numpy as np
    from scipy.ndimage import filters
    import cv2
except ImportError:
    print("No numpy or opencv installed. Data will be sent as raw bytes")

# Settings
# --------------------------------------------------

# Output video resolution
WIDTH = 1280
HEIGHT = 720

# Camera settings
CAMERA_NUMBER = 0

# TCP port for server
PORT = 8888

# --------------------------------------------------
# End of settings

# Check for command line arguments
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])

print("Starting server on port", PORT)

# Connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)
print("Waiting for client to connect...")

# Wait for client
conn, addr = s.accept()
print("Connected to", addr)

# Get video capture
