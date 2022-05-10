import socket
import sys
import time

def check_host(host, port):
    """
    Given a host and port, returns whether the port is open on the host.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
        return True
    except socket.error:
        return False

def wait_for_port(host, port, timeout=10, wait=1):
    """
    Wait for a port to open on a host.
    """
    start = time.time()
    while not check_host(host, port):
        if time.time() - start > timeout:
            raise Exception("Could not connect to: %s:%s" % (host, port))
        time.sleep(wait)

def wait_for_server(host, port, timeout=10, wait=1):
    """
    Wait for a server on host:port to respond with a 200.
    """
    wait_for_port(host, port)
