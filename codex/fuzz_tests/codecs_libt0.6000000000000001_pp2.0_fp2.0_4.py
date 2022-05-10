import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import sys
# import mysql.connector
# from mysql.connector import errorcode
# from mysql.connector.pooling import MySQLConnectionPool

# from config import *

# try:
#     cnx = mysql.connector.connect(**config)
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#     pool = MySQLConnectionPool(pool_name="mypool", pool_size=3, **config)

#     cursor = cnx.cursor()

#     cursor.execute("DROP TABLE IF EXISTS writers")
#     cursor.execute("CREATE TABLE writers
