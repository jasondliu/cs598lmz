import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# con = sqlite3.connect('test.db')
# cur = con.cursor()
# cur.execute('''
# CREATE TABLE stocks
# (date text, trans text, symbol text, qty real, price real)
# ''')
# con.commit()
# data = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#         ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#         ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#       ]
# cur.executemany("INSERT INTO stocks VALUES (?,?,?,?,?)", data)
# con.commit()

# so_path = ctypes.util.find_library('libqlibc.so')  
so_path = "./libqlibc.so"

lib = ctypes.CDLL(so_path)

