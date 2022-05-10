import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Desktop/data.db")

# Define the function to be used in the thread
def get_data():
    # Get the data from the database
    db = sqlite3.connect("/home/pi/Desktop/data.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    db.close()
    return data

# Define the function to be used in the thread
def get_data_test():
    # Get the data from the database
    db = sqlite3.connect("/home/pi/Desktop/data.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM data_test")
    data = cursor.fetchall()
    db.close()
    return data

# Define the function to be used in the thread
def get_data_update():
    # Get the data from the database
    db = sqlite3.connect("/home/pi/Desktop/data.db")
    cursor = db.cursor()

