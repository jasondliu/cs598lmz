import socket
import time
import random

# Setup connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.104', 8888))

# Run forever
while True:
    # Generate random integer
    value = random.randint(0, 1023)

    # Send value to server
    s.send(bytes(str(value), 'utf-8'))

    # Wait 1 second
    time.sleep(1)

# Close connection
s.close()
