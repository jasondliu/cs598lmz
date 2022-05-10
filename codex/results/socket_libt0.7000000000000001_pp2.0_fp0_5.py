import socket, sys, struct, select, string

'''
To connect to the server, you use
$ python3 client.py <server> <port> <tokens>

Where <tokens> is a string of space-separated tokens.

'''

def main(argv=sys.argv):
    server = argv[1]
    port = int(argv[2])
    tokens = argv[3:]

    if len(tokens) == 0:
        print("No tokens provided")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((server, port))
    s.settimeout(None)

    # create the message
    msg = " ".join(tokens)

    # send the message
    send_message(s, msg)

    # receive the results
    print("Received results:")
    while True:
        # receive a message
        try:
            # receive a message
            msg = recv_message
