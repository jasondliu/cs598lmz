import select
# Test select.select() for client program

import socket
import select
import sys
import string

# List all the active ports

SERVER = 'irc.freenode.net'
PORT = 6667
NICK = 'randy1'
CHANNEL = '#cs330'

# Create a new socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the IRC server
s.connect((SERVER, PORT))

s.setblocking(0)	# Set to non-blocking mode

# Send data to the server
s.send('NICK ' + NICK + '\r\n')
s.send('USER ' + NICK + ' ' + NICK + ' ' + NICK + ' :Python IRC\r\n')
s.send('JOIN ' + CHANNEL + '\r\n')

# Main loop

while True:

	# Get to put in input
	buffer = raw_input()
	buffer = buffer.strip()
	# Print server response
