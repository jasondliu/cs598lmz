import socket
import threading
import tkinter
from tkinter import *
import sys

class Server():
    def __init__(self):
        self.host = ""
        self.port = 9999
        self.s = socket.socket()
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        self.c, self.addr = self.s.accept()
        print("Connection from: " + str(self.addr))
        self.chat_window = Tk()
        self.chat_window.title("Server")
        self.chat_window.geometry("500x500")
        self.text = Text(self.chat_window)
        self.text.pack()
        self.entry = Entry(self.chat_window)
        self.entry.pack()
        self.mybtn = Button(self.chat_window, text="send", command=self.send)
        self.mybtn.pack()
        t1 = threading.Thread(target=self.receive)
        t1.start
