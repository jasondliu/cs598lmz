import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Desktop/Data_log.db")

# Define the function to be threaded
def threaded_function(arg):
    for i in range(arg):
        print("running")
    return

# Define the function to be threaded
def threaded_function_2(arg):
    for i in range(arg):
        print("running 2")
    return

if __name__ == "__main__":
    # threading.Thread(target = threaded_function, args = (10, )).start()
    # threading.Thread(target = threaded_function_2, args = (10, )).start()
    # print("done")
    # libc = ctypes.CDLL(ctypes.util.find_library('c'))
    # libc.prctl(1, 15)
    # print("done")

    # Connect to the database
    db = sqlite3.connect("/home/pi/Desktop/Data_log.db")

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL statement
   
