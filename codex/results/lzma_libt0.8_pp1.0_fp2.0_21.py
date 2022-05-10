import lzma
lzma.LZMAFile('jeopardy.xz').read()
"""

import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute(
    """
    SELECT * FROM game_log LIMIT 0
    """
)
print(cursor.fetchall())

cursor.execute(
    """
    SELECT * FROM person_appearance LIMIT 0
    """
)
print(cursor.fetchall())

connection.close()
