import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# def test():
#     conn = sqlite3.connect('db/test.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#     conn.commit()
#     conn.close()

# test()

# Test plt + mpld3
# import matplotlib.pyplot as plt
# import mpld3

# def test():
#     plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
#     mpld3.show()

# test()

# Test ctypes + PLplot
# plplot = ctypes.cdll.LoadLibrary(ctypes.util.find_library('plplotd'))

# def test():
#     plplot.plinit()
#     plplot.plenv(0, 1, 0, 1, 0, 0)
#     plplot.plline([0.1, 0
