import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# https://docs.python.org/3/library/ctypes.html
# https://docs.python.org/3/library/sqlite3.html

class Player:
    def __init__(self, name, sock):
        self.name = name
        self.sock = sock
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE players (name TEXT PRIMARY KEY, score INTEGER)")
        self.cursor.execute("INSERT INTO players VALUES (?, ?)", (name, 0))
        self.conn.commit()

    def score(self, score):
        self.cursor.execute("UPDATE players SET score = score + ? WHERE name = ?", (score, self.name))
        self.conn.commit()

    def get_score(self):
        self.cursor.execute("SELECT * FROM players WHERE name = ?", (self.name,))
        return self.cursor.fetchone()
