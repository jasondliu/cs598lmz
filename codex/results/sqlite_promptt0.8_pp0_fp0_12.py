import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

db = sqlite3.connect(':memory:')
cur = db.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY, id_string TEXT, title TEXT, description TEXT, done INTEGER)')
db.commit()
db.row_factory = sqlite3.Row

# Test load
todo0 = {
    'id_string': '1234567890123456789012345678901234567890',
    'title': 'Test',
    'description': 'Create a Todo object to be manipulated',
    'done': 0
}

# Test savedb and loaddb
cur.execute('INSERT INTO todo(id_string, title, description, done) VALUES(:id_string, :title, :description, :done)', todo0)
db.commit()
cur.execute('SELECT * FROM todo WHERE id_string=:id_string', todo0)
tt = cur.fetchone()

# Test save
todo
