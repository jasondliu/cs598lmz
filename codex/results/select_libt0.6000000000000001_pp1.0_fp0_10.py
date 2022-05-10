import selectors
import socket
import types
import sys

from threading import Thread

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

from ttkthemes import ThemedTk


class Client:
    def __init__(self, master, host, port):
        self.master = master
        self.master.title("File Sharing Client")
        self.master.geometry("400x320")

        self.host = host
        self.port = port

        self.messages = []

        self.create_widgets()
        self.create_socket()

    def create_widgets(self):
        self.create_menubar()
        self.create_frame()
        self.create_connection_label()
        self.create_host_entry()
        self.create_port_entry()
        self.create_connect_button()
        self.create_file_label()
        self.create_
