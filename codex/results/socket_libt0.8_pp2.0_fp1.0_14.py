import socket
from threading import Thread
from PIL import Image
import io
import time


def TCP_connect(ip, port_number, timeout=0.5, coding='utf-8'):
    """
    create a connection with a host
    :param ip: ip address of a host
    :param port_number: the port number of a host
    :param timeout: timeout for the socket to connect
    :param coding: the coding for data translation
    :return: connected socket
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(timeout)
    client_socket.connect((ip, port_number))
    return client_socket, coding


def send_msg(sock, msg, coding='utf-8'):
    """
    send msg to host
    :param sock: socket connected to a host
    :param msg: msg to send
    :param coding: msg coding
    :return:
    """
    if type(msg) == list:
        msg = " ".join(msg)
