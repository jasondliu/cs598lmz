import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('map.db'), in which a table named 'map' exists
# CREATE TABLE map (ID INTEGER PRIMARY KEY AUTOINCREMENT, dest VARCHAR(256));
def ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)
        s.connect(('10.255.255.255', 0))
        myip = s.getsockname()[0]
    except:
        print('failed to get ip address')
        return None
    finally:
        s.close()
    return myip

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def send_periodically(f, args, period):
    #global sock
    sock = f(*args)
    timer = threading.Timer(period, send_periodically,[f, args, period])
    timer.daemon = True
    timer.start()
    #sock.close()

def send
