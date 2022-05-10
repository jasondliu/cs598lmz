import socket
import time
import RPi.GPIO as GPIO
from time import sleep

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.0.101', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

servoPIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 26 for PWM with 50Hz
p.start(0) # Initialization

while True:

    print('\nWaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    if data:
        p.ChangeDutyCycle(float(data))
        print('sent {} back to {}'.format
