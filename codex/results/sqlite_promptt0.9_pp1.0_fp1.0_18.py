import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() no parametros
conn = sqlite3.connect()
cursor = conn.cursor()
# Test sqlite3.connect() com parametros
conn = sqlite3.connect(database='foo.db')
cursor = conn.cursor()
# Teste do sqlite3.connect() com parametros
conn = sqlite3.connect(database='foo.db', check_same_thread=False)
cursor = conn.cursor()
# Teste do sqlite3.connect() com parametros
conn = sqlite3.connect(database='foo.db', check_same_thread=False,
                       factory=None, cached_statements=100)
cursor = conn.cursor()
# Teste do sqlite3.connect() com parametros
conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()
# Teste do sqlite3.connect() com parametros
conn = sqlite3.connect(database='foo.db', check_same_thread=False)
cursor = conn
