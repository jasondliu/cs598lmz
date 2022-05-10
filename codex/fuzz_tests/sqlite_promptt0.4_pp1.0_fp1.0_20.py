import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Test sqlite3.connect()

# Test sqlite3.connect()

# Test sqlite3.connect()

# Test sqlite3.connect()

# Test sqlite3.connect()

# Test sqlite3.connect()

# Test sqlite3.connect()

# Test sqlite3.connect()

# Test sqlite3
