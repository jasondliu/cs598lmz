import select
import socket
import sys

# Read a message from stdin and decode it. Returns None on EOF.
def getMessage():
    next_line = sys.stdin.readline()
    if not next_line:
        return None
    return next_line.strip()

# Encode a message for transmission, given its content.
def encodeMessage(messageContent):
    encodedContent = messageContent.encode('ascii')
    header = f"{len(encodedContent):<{HEADERSIZE}}".encode('ascii')
    return header + encodedContent

# Send an encoded message to the server.
def sendMessage(message):
    message = message.encode('ascii')
    # We need to read the response first
    while True:
        # Read the response.
        ready = select.select([sock], [], [], 0.5)
        if ready[0]:
            response = sock.recv(HEADERSIZE)
            if len(response) == 0:
                print('Disconnected from server.')
                sys.exit()

