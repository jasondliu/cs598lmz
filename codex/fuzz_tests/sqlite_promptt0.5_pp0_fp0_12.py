import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(:memory:)

# TODO: 
#   - create a database instance
#   - create a database connection
#   - create a database cursor
#   - create a table
#   - insert a row
#   - select a row
#   - update a row
#   - delete a row
#   - close the database connection

class database(object):
    def __init__(self, filename):
        self.filename = filename
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        
    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()
        
    def __del__(self):
        self.close()
        
def main():
    db = database(':memory:')
    db.execute('CREATE TABLE foo (bar STRING);')
    db.execute('INSERT INTO foo VALUES ("
