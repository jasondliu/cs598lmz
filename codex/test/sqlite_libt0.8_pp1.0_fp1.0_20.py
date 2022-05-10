import ctypes
import ctypes.util
import threading
import sqlite3

# Load the script's classes
import libnfc
import sqlite3, os

# Load the script's functions
from function_rfid import *
from function_mail import *
from function_sql import *

# Load the script's parameters
from param import *

# Open SQL DB
conn = sqlite3.connect(db)
cursor = conn.cursor()

# Initialize RFID libnfc
libnfc.rfid_init(nfc_conf)

# Launch thread to read the RFID chip
T1 = threading.Thread(name='loop_rfid', target=loop_rfid)
T1.daemon = True
T1.start()

while 1:
    
    conn.commit()
    cursor.execute('''SELECT id, KLAUDIO_UID, KLAUDIO_MAIL, KLAUDIO_NAME, DATE() FROM id''')
    #cursor.execute('''SELECT id, KLAUDIO_UID, KLAUDIO_MAIL, KLAUDIO_NAME FROM id''')
   
