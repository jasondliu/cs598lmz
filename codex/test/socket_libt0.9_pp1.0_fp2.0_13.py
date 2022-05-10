import socket
from multiprocessing import Process
import struct
import plotly.plotly as py
import plotly.graph_objs as go
import datetime
import os
from plotly.graph_objs import Layout, Data, Figure, Stream, YAxis
import RPi.GPIO as GPIO
from datetime import datetime as dt

py.sign_in("emmellito", "alwgjlcwtn")


def receive_data(conn, end_cond=None):
    total_data = []
    data = ''

    while True:
        data = conn.recv(1024)
        if end_cond(data):
            break

        if len(data) > 0:
            total_data.append(data)

    return total_data


def recv_msg(conn, end_cond=None):
    total_data = receive_data(conn, end_cond)

    return ''.join(total_data)


