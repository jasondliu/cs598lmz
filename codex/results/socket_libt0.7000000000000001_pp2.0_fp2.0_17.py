import socket
import time
import math

# get the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.0.10", 4765))

# send command to start the stream
s.send("\r\n\r\n")
time.sleep(0.1)

# get the stream
data = ""
while True:
    data += s.recv(8192)
    time.sleep(0.01)
    if data.endswith("\r\n"):
        break

# parse the data
data = data.split("\r\n")[1:-1]
data = [l.split(" ") for l in data]
data = [(float(l[0]), float(l[1]), float(l[2]), float(l[3])) for l in data]

# calculate the number of data points
# and the sample frequency
n = len(data)
fs = n / data[-1][0]

# calculate the frequency response
pad = False

