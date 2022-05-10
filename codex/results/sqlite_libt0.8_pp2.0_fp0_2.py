import ctypes
import ctypes.util
import threading
import sqlite3
import sqlite
from Tkinter import *
import tkMessageBox
from PIL import ImageTk,Image
from threading import Timer


class App:


	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.master = master
		self.conn = None
		self.is_playing = False
		self.current_song = 0
		self.current_song_time = 0
		self.current_song_length = 0
		self.last_db_timestamp = 0
		self.current_song_path = None
		self.current_song_artist = None
		self.user_id = None
		self.auto_mode = False
		self.auto_mode_active = False
		self.left_bar_active = False

		self.master.title("tune&mood")
		self.master.geometry("300x300")
		self.master.resizable(width = FALSE, height = FALSE)
