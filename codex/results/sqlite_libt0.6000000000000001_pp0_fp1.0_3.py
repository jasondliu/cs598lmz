import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

# TODO:
#  - Search for images in subdirectories
#  - Use the actual database, not the SQLite database
#  - Use the database for thumbnails, not the actual images
#  - Add a progress bar
#  - Add a status bar
#  - Add a menu

class Database:
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(database)
        self.connection.text_factory = str
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute('select count(*) from images')
        except sqlite3.OperationalError:
            self.cursor.executescript('''
                create table images (
                    id integer primary key,
                    filename text not null,
                    width integer not null,
                    height integer not null,
                    thumbnail blob,
                    thumbnail_width integer,
                    thumbnail_height integer,
                    thumbnail_updated integer
                );

                create index images_filename_index on images
