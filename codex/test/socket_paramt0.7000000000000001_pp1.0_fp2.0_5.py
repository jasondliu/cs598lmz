import socket
socket.if_indextoname(1)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-m", "--mac", type=str, help="MAC address for the interface to use", required=True)
    parser.add_argument("-p", "--port", type=int, help="Port to listen on", default=8080)
    parser.add_argument("-f", "--file", type=str, help="File to save to", default="output.bin")
    parser.add_argument("-a", "--all", help="use the all-zero MAC address", action="store_true")
    args = parser.parse_args()

    if args.all:
        if args.verbose:
            print("Using all-zero MAC address")
        mac = "00:00:00:00:00:00"

