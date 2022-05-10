import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db = sqlite3.connect(":memory:")
# create database table
db.execute('''CREATE TABLE data (
  Timestamp DATETIME,
  Datatype TEXT,
  Data TEXT,
  Sensor TEXT
  )''')

# create datagenerator threads
inclinometer = Inclinometer('inclinometer')

# setup datagenerators
inclinometer.start()


# main loop

while True:
    # read from database
    cursor = db.execute('SELECT Timestamp, Datatype, Data, Sensor FROM data')
    for row in cursor:
        print(row)
    time.sleep(2)
    print(inclinometer.running)
    if not inclinometer.running:
        break

# save changes to database
db.commit()

# close database
db.close()
