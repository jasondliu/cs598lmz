import ctypes
ctypes.windll.shell32.IsUserAnAdmin()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from shutil import copyfile
from subprocess import call, Popen, PIPE
from xml.etree import ElementTree as ET
import os, sys, datetime, shutil, time, psutil, traceback, subprocess
from time import sleep
from zipfile import ZipFile
import threading
import ctypes
from ctypes import wintypes, windll
from platform import release
import netifaces as ni


class Ui_MainWindow(object):
    def __init__(self):
            # variables
        self.force_stop=0
        self.is_directory=0
        self.is_running=0
        self.is_server_running=0
        self.log_path=os.path.join(os.path.expanduser("~"),"Desktop")
        self.pixels=1
        self.wdt_time=30
        self.WDT_TIMER=self.wdt_time

