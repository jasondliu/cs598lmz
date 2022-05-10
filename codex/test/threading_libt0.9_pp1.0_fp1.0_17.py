import threading
threading._DummyThread._Thread__stop = lambda x: 42

import sys
sys.path.append("..")
import os
import base64
import uuid
import json
import requests
import hashlib
import PIL.Image
import PIL.ImageTk
from subprocess import check_output
import webbrowser

from client.common import*
from client.main import*
from preferences.common import*
from preferences.services import*
from preferences.communicator import*

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image



class ViewService(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.winfo_toplevel().title("View Services")

        self.frames = {}
