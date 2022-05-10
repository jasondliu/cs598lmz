import socket
import sys
import thread

# default host
HOST = '0.0.0.0'  
PORT = 27000

def check_for_command(data):
    if data == 'close':
        sys.exit()

def accept_connection(sock):
    """
    Accept as many clients as possible.
    """
    while True:
        # block until client is connected
        conn, addr = sock.accept()
        # start listening to client in new thread
        thread.start_new_thread(start_listening, (conn, addr))

def start_listening(conn, addr):
    """
    Receive messages from clients in a loop until 'close' is received.
    """
    while True:
        data = conn.recv(1024)
        if data:
            check_for_command(data)
            print('<', addr, '>', data)
        else:
            break
    conn.close()

