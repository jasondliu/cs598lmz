import sys, threading
threading.Thread(target=lambda: sys.stdout.buffer.write(sys.stdin.buffer.read())).start()
'''


def TCP_Connect(ip, port_number, delay, count):
    TCPsock = socket(AF_INET, SOCK_STREAM)
    TCPsock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        return True
    except:
        if count >= 1:
            TCP_Connect(ip, port_number, delay, count - 1)


def scan_port(host_ip, delay, port):
    try:
        if TCP_Connect(host_ip, port, delay, 2):
            return True
        else:
            return False
    except:
        return False


# getting command line arguments
parser = argparse.ArgumentParser(description="Port Scanner")
parser.add_argument('-H', '--host', help='Target Host', required=True)
parser.add_
