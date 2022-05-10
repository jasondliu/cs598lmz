import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/aaron/Desktop/blah/test.sqlite3')

# TODO: Make a basic GUI (Tkinter?) to display the output.

# TODO: Figure out how to determine the name of the current file for the
# database.
# TODO: Make it so that it quits after all of the modules have been finished
# with.

# TODO: Make it so that it can tell if the process is running.

# TODO: Make it so that the program will output to a database
# instead of the terminal.

# TODO: Make it so that it will work on windows

# TODO: Make it so that it can read the database, and convert it to regular
# text.

# TODO: Make it so that it can record keystrokes.

# TODO: Make it so that it can record the screen.

class ProcessMonitor(threading.Thread):
    """
    A class used to monitor the processes currently running.
    It will keep track of the time that the process has been running
    for, and the name of the process.
   
