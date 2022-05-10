import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")

# TODO:
# - Add 'queue' to allow multiple commands to be sent at once (like a batch)
# - Add 'wait' to allow for commands to be sent in sequence
# - Add 'exit' to close the connection
# - Add 'help' to display a help message
# - Add 'clear' to clear the screen
# - Add 'log' to display the log file
# - Add 'config' to display the config file
# - Add 'cd' to change directory
# - Add 'ls' to list files
# - Add 'pwd' to display the current directory
# - Add 'cat' to display a file
# - Add 'rm' to delete a file
# - Add 'mv' to move a file
# - Add 'cp' to copy a file
# - Add 'mkdir' to create a directory
# - Add 'rmdir' to delete a directory
# - Add 'mvdir' to move a directory
# - Add 'cpdir' to copy a directory
# - Add 'find' to find a file
# - Add 'grep' to grep
