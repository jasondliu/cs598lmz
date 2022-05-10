import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import getopt

#
# This is the main function
#
def main(argv):
    #
    # The first thing we need to do is to create the database
    #
    db = sqlite3.connect('/home/pi/robot_database.db')
    cursor = db.cursor()
    #
    # Create the table
    #
    cursor.execute('''CREATE TABLE IF NOT EXISTS ROBOT_COMMANDS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        COMMAND TEXT NOT NULL,
        PARAMETER TEXT NOT NULL);''')
    db.commit()
    #
    # Now we will create the threads
    #
    # The first thread is the one that will be listening for commands
    #
    #
    # This is the thread that will be listening for commands
    #
    listen_thread = threading.Thread(target=listener)
    listen_thread.start()
    #
    # This is the thread that will be sending data
    #
