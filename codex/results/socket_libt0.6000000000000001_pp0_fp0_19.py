import socket
import threading
import time

from pymavlink import mavutil
from dronekit import connect, VehicleMode, LocationGlobalRelative

# Connect to the Vehicle.
print("Connecting to vehicle on: serial0")
vehicle = connect('/dev/serial0', wait_ready=True, baud=57600)

# Open UDP socket
UDP_IP = "192.168.2.2"
UDP_PORT = 8888
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# Create a message listener for all messages.
@vehicle.on_message('*')
def listener(self, name, message):
    print 'message: %s' % message

def send_attitude_target(roll_angle = 0.0, pitch_angle = 0.0,
                         yaw_angle = None, yaw_rate = 0.0, use_yaw_rate = False,
                         thrust = 0.5):

