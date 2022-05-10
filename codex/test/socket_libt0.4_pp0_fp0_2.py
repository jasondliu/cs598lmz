import socket
import sys
import time
import threading
import os
import math

from Tkinter import *

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Create a Tkinter window
window = Tk()
window.title("Client")
window.geometry("300x200")

# Create a label
label = Label(window, text="")
label.pack()

# Create a button
button = Button(window, text="Send", command=lambda: send_message(sock, label))
button.pack()

# Create a text entry box
text = Entry(window)
text.pack()

# Create a text entry box
text2 = Entry(window)
text2.pack()

# Create a text entry box
