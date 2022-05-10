import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# cnxn = sqlite3.connect('C:\\Temp\\Test.db')
# cursor = cnxn.cursor()
# cursor.execute("CREATE TABLE tblNames(Name varchar(25) NOT NULL, Description varchar(25) NOT NULL)")
# cursor.execute("INSERT INTO tblNames(Name, Description) VALUES (?,?)", ('Joe', 'Tester'))
# cursor.execute("INSERT INTO tblNames(Name, Description) VALUES (?,?)", ('Sue', 'Tester'))
# cursor.execute("INSERT INTO tblNames(Name, Description) VALUES (?,?)", ('Fred', 'Tester'))
# cnxn.commit()
# cursor.execute("SELECT Name FROM tblNames")
# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print(row[0]) 
# # cnxn.close()
# try:
#     connection = sqlite3.connect('C:\\Temp\\Test.db')
#    
