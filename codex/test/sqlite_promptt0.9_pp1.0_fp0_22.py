import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection(with history disabled)
conn = sqlite3.connect(':memory:', check_same_thread=False)
c = conn.cursor()
c.execute('''create table test (id real, name varchar(10))''')
sql = 'insert into test (id,name) VALUES (?,?)'
c.execute(sql,(1,"Chicho"))
c.execute(sql,(2,"Blanca"))
c.execute(sql,(3,"Julieta"))
c.execute(sql,(4,"Caigù"))

conn.commit()
conn.close()
crypto = ctypes.CDLL(ctypes.util.find_library('crypto'))
ssl = ctypes.CDLL(ctypes.util.find_library('ssl'))

# Change the commonName according to the name stored in the certificate 
# in PEM format you are using.
get_certificate_subject = lambda x : crypto.X509_get_subject_name(x).decode('utf8', 'strict').split('/CN=')[1]


