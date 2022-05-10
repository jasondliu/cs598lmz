import socket
# Test socket.if_indextoname()
from socket import if_indextoname, if_nameindex
from time import time


def main():
    # Get the first interface name
    if_idx = if_nameindex()[0][0]
    ifname = if_indextoname(if_idx)

    if ifname.startswith("lo"):
        print("skipping loopback interface")
        return

    # Create a raw socket for the interface
    sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(3))
    # https://stackoverflow.com/questions/38380607/error-socket-error-protocol-not-available
    #  # htons(3) = 3: filter for incoming packets with proto number 3
    # Bind it to the interface
    sock.bind((ifname, 0))

    # Initialize the start time
    start_time = time()
    # Initialize the counters for received and transmitted packets
    rx_packets = 0
    tx_packets = 0

    # Fetch the
