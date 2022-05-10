import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection()
#con = sqlite3.connect(":memory:")
#cur = con.cursor()
#cur.execute("create table foo (id INTEGER PRIMARY KEY);")
#cur.execute("insert into foo (id) values (1);")
#cur.execute("insert into foo (id) values (2);")
#cur.execute("select id, id*3 as f1 from foo where id=1")
#print cur.fetchone()


#ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

class SerialThread(threading.Thread):
    def __init__(self, ser):
        threading.Thread.__init__(self)
        self.ser = ser
        self.running = True
        self.data_available = threading.Event()
        self.data = []
        self.send = []
    def run(self):
        while self.running:
            if len(self.send) > 0:
                self.ser.write(self.send.pop(0))
