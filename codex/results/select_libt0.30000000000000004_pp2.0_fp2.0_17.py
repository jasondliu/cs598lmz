import select
import socket
import sys
import threading
import time
import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsg
import tkinter.filedialog as tkfile
import tkinter.simpledialog as tksimple
import tkinter.colorchooser as tkcolor
import tkinter.font as tkfont
import tkinter.ttk as ttk
import tkinter.ttk as ttk
import tkinter.ttk as ttk
import tkinter.ttk as ttk
import tkinter.ttk as ttk

# クライアント側のソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# サーバー側のソケットを作成
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#
