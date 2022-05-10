import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys

# import MySQLdb

# import pymysql
# pymysql.install_as_MySQLdb()

# import MySQLdb
# db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql")
# cur = db.cursor()
# cur.execute("SELECT Host,User FROM user")
# for row in cur.fetchall():
#     print(row[0], row[1])

#
# def create_connection():
#     """ create a database connection to the SQLite database
#         specified by the db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)
#
#     return None
#
#
# def select_all_t
