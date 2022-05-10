import socket
import pickle

# IP and port of Tello
tello1_address = ('192.168.10.1', 8889)
tello2_address = ('192.168.10.2', 8889)
tello3_address = ('192.168.10.3', 8889)
tello4_address = ('192.168.10.4', 8889)
tello5_address = ('192.168.10.5', 8889)

# IP and port of local computer
local1_address = ('', 9000)
local2_address = ('', 9001)
local3_address = ('', 9002)
local4_address = ('', 9003)
local5_address = ('', 9004)

# Create a UDP connection that we'll send the command to
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
