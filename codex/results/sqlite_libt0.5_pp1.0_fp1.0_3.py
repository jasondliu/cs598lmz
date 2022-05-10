import ctypes
import ctypes.util
import threading
import sqlite3


class Location(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return "%s,%s" % (self.latitude, self.longitude)


class LocationDatabase(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS locations (
                latitude REAL,
                longitude REAL,
                timestamp INTEGER
            )
        """)

    def add_location(self, location):
        self.conn.execute("INSERT INTO locations VALUES (?, ?, ?)",
                          (location.latitude, location.longitude,
                           int(time.time())))
        self.conn.commit()

    def get_locations(self):
        locations = []
        for row in self.conn.execute("SELECT * FROM locations"):
