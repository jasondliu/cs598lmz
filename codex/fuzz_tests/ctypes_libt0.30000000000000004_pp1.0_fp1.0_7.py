import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Title", "a Tk MessageBox")

# https://stackoverflow.com/questions/14058453/making-python-to-wait-to-finish-a-function
import time
time.sleep(5) # delays for 5 seconds

# https://www.geeksforgeeks.org/python-wait-for-a-specific-time-in-python/
import datetime

# Wait for a specific time
# Time format -> Hour:Minute:Second
# Eg. 14:30:00
# Eg. 00:30:00

# Current time
now = datetime.datetime.now()

# Time to wait
wait_time = datetime.time(14, 30, 00)

# Convert to datetime format
wait_time = datetime.datetime.combine(datetime
