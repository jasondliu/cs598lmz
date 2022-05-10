import socket
import sys
import time
import threading
import argparse

class Client(threading.Thread):
    def __init__(self, server_ip, server_port, file_name, window_size, timeout):
        threading.Thread.__init__(self)
        self.server_ip = server_ip
        self.server_port = server_port
        self.file_name = file_name
        self.window_size = window_size
        self.timeout = timeout
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.settimeout(timeout)
        self.seq_num = 0
        self.ack_num = 0
        self.base = 0
        self.next_seq_num = 0
        self.send_base = 0
        self.last_ack_received = 0
        self.last_ack_sent = 0
        self.last_ack_received_time = 0
        self.last_ack_sent_time = 0
        self.last_
