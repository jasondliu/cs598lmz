import socket
import sys


def main():
    if len(sys.argv) != 2:
        print("expected format: 'script, IP address'")
    host = sys.argv[1]

    try:
        IP = socket.gethostbyname(host)
        print("The IP Address is: ", IP)
    except socket.error:
        print("Host could not be resolved")


if __name__ == '__main__':
    main()
