import socket
import struct
import config
import keys

MAX_PACKET = 2048

def irRx():
    udp_ir_endpoint = config.udp_ir_endpoint
    cmd_ir_endpoint = config.cmd_ir_endpoint

    server = config.server

    # initialize the UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if server != None:
        print("You are a server")
        if (udp_ir_endpoint != None):
            print("  binding to UDP port: %i"%udp_ir_endpoint)
            sock.bind(("", udp_ir_endpoint))

        # listen for incoming commands on the TCP port
        if (cmd_ir_endpoint != None):
            print("  listening on TCP port: %i"%cmd_ir_endpoint)
            serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
