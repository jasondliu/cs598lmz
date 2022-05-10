import socket
import sys
import time
import threading
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import subprocess
from multiprocessing import Process, Queue
from threading import Thread
from multiprocessing.connection import Listener
from multiprocessing.connection import Client
from multiprocessing.connection import Listener
from multiprocessing.connection import Client
import pickle

class chat_client(object):
    def __init__(self, host_ip, host_port, my_ip, my_port):
        self.host_ip = host_ip
        self.host_port = host_port
        self.my_ip = my_ip
        self.my_port = my_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host_ip, host_port))
        self.root = Tk()
        self.root.title("Client")

