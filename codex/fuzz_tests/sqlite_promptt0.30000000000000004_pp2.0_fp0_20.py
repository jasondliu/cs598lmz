import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Database
DB_NAME = "test.db"

# Table
TABLE_NAME = "test"

# Columns
COLUMN_ID = "id"
COLUMN_NAME = "name"
COLUMN_AGE = "age"

# Create table
CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + "(" \
                   + COLUMN_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " \
                   + COLUMN_NAME + " TEXT NOT NULL, " \
                   + COLUMN_AGE + " INTEGER NOT NULL)"

# Insert data
INSERT_DATA_SQL = "INSERT INTO " + TABLE_NAME + "(" + COLUMN_NAME + ", " + COLUMN_AGE + ") VALUES(?, ?)"

# Query data
QUERY_DATA_SQL = "SELECT * FROM " + TABLE_NAME

# Delete data
DELETE_DATA_SQL = "DELETE FROM " + TABLE_NAME

# Update data
UPDATE_DATA_
