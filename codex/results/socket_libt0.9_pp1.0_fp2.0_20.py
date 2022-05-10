import socket
import threading
import time


# This two arguments are required for starting the program.
# You need to specify one of them or both of them.
# If you omit them, the program will print out a help menu instead.
ap_address = None
target_address = None

# port number
target_port = None


def parse_arguments():
    global ap_address
    global target_address
    global target_port

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "ha:t:p:",
            ["ap=", "target=", "port="]
        )
    except getopt.GetoptError as e:
        print('replay_attack.py -a <AP address> -t <target address> -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('replay_attack.py -a <AP address>  -t <target address> -p <port>')
            sys.exit
