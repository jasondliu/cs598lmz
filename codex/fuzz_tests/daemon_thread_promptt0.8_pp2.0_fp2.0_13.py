import threading
# Test threading daemon
import time
import numpy as np  
from scipy.interpolate import interp1d


# setup socket communication
server_ip = '192.168.1.8'
server_port = 502
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))

# setup threading
t1 = threading.Thread(target=read_data, args=(s,))
t1.start()

# set up pid and motor_control

# pid setup
k = 0.1  # proportional constant
e = 0    # error variable

x = list()
y = list()
t = list()

# read joint angles and record them
for i in range(40):
    # convert byte to float
    ang_byte = s.recv(8)
    ang = struct.unpack("d", ang_byte)[0]
    x.append(ang)
    time.sleep(0.01)
    # calculate proportional error, the error is between desired angle and the present angle

