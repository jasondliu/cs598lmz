import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
print "Creating database..."
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''create table stocks
             (date text, trans text, symbol text,
              qty real, price real)''')
c.execute("""insert into stocks
                  values ('2006-01-05','BUY','RHAT',100,35.14)""")
conn.commit()
print "Created database.\n"

with conn:
    c.execute("SELECT * FROM stocks")
    print c.fetchall()

# From: https://github.com/VladimirZouev/python-libspotify
# Copyright (c) 2013, Vladimir Zouev
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#    Redistributions in binary form must reproduce the above copyright
#    notice, this list of
