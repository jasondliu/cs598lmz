import socket, json, argparse, sys, struct, os

# TODO:
#   1. Make the client be able to handle multiple files
#   2. Make the server be able to handle multiple files
#   3. Make the client send a list of files to the server
#   4. Make the server send a list of files to the client
#   5. Make the client send a single file to the server
#   6. Make the server send a single file to the client
#   7. Make the client send a list of files to the server
#   8. Make the server send a list of files to the client
#   9. Make the client send multiple files to the server
#   10. Make the server send multiple files to the client

# This function is used to send a message to the server
def sendMessage(sock, message):
    # Encode message to bytes and send it
    sock.sendall(message.encode())

# This function is used to receive a message from the server
def receiveMessage(sock):
    # Receive the message
    message = sock.recv(1024)

