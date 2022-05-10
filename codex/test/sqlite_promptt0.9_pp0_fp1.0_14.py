import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('mysqlite.db')
# sys.argv[0] just in case there are any command line args passed.
path_to_lib = '/usr/local/lib/libsqlcipher.so'
# Open the encrypted database...
db_name = 'mysqlite.db'
libsql = ctypes.cdll.LoadLibrary(path_to_lib)
# Do this once!
libsql.sqlite3_key("mysqlite.db", "passwd") # hardcoded passwd for the random
# db lol...
pdb = sqlite3.connect(db_name)
cur = pdb.cursor()
#pdb.row_factory = sqlite3.Row
def get_results():
    cur.execute("SELECT * from sqlite_master")
    results = cur.fetchall()
    return results

def get_data():
    cur.execute("SELECT * from data")
    results = cur.fetchall()
    return results
#print (get_results())
#pdb.close(pdb)
