import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("database.db")
##database = sqlite3.connect("database.db")
##cursor = database.cursor()
##sql = """INSERT INTO Test (Test1, Test2) VALUES("This", "That")"""
##cursor.execute(sql)
##database.commit()
##cursor.close()
##database.close()
##print("done")
import time
def main():
    SETUPDLL = ctypes.CDLL("setup_win.dll")
    SERIALDLL = ctypes.CDLL("serial_win.dll")
    SETUPRETURN = SETUPDLL.main()
    global t1
    if SETUPRETURN == 0:
        t1 = threading.Thread(target=SERIALDLL.readserial)
        t1.start()
##        t2 = threading.Thread(target=setDatabase, daemon = True)
##        t2.start()
        while True:
            pass
    else:
        print("could not setup")
    
##def setDatabase():
##    database = sqlite3.connect
