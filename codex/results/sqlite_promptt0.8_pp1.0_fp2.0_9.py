import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    # Create table
    cur.execute("CREATE TABLE IF NOT EXISTS config (module text primary key, config text)")
    # Get configuration from table or return None
    cur.execute("SELECT config FROM config WHERE module = 'Configuration'")
    config = cur.fetchone()
    # TODO: Complete the parser
    #if not config:
    #    config = [1, 2, 3, 4, 5, 6, 7, False, False, False]
    #else:
    #    config = config[0].split("|")
    #    config[6] = config[6] == "True"
    #    config[7] = config[7] == "True"
    #    config[8] = config[8] == "True"
    # Insert new configuration or update existing one
    #cur.execute("INSERT OR REPLACE INTO config (module, config) VALUES (?, ?)", ("Configuration", "|".join(map(str, config))))

