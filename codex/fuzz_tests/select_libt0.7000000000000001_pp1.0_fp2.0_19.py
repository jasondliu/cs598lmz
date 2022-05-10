import select
import sys
import time
import gc
from tzlocal import get_localzone
import sqlite3 as lite

def getData():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return (humidity, temperature)


def getSQLData():
    con = lite.connect('/home/pi/Documents/temp/temp.db')
    con.row_factory = lite.Row
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM temp ORDER BY id DESC LIMIT 1")

    rows = cur.fetchall()
    for row in rows:
        humidity = row["humidity"]
        temperature = row["temperature"]
  
    return (humidity, temperature)
        
def getCurrent():
    humidity, temperature = getSQLData()
    local_time = get_localzone().localize(datetime.now())
    current = {"temperature":temperature,"humidity":humidity,"time":local_time}
    
    return current
    
def getHistory
