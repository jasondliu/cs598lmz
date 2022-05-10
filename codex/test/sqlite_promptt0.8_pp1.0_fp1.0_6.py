import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and cursor.execute()
# https://stackoverflow.com/questions/29213707/how-do-i-create-sqlite-database-with-python
# https://stackoverflow.com/questions/11532895/retrieve-an-arbitrary-row-from-a-sqlite-database-in-python
# https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
#
#   create table sensor(sensorID VARCHAR(255), description VARCHAR(255));
#   insert into sensor(sensorID, description) VALUES("0123456789abcde", "sensor01");
#   insert into sensor(sensorID, description) VALUES("fedcba9876543210", "sensor02");
#   insert into sensor(sensorID, description) VALUES("1234567890abcde", "sensor03");
#   insert into sensor(sensorID, description) VALUES("1234567890abcd0", "sensor04");
#  
