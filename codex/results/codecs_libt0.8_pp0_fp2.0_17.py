import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

# Import packages
import MySQLdb
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, types



# Connect to the database
def connect(user, pwd, host, db):
    """
    Makes a connection to a database.

    :param user: str, username
    :param pwd: str, password
    :param host: str, hostname
    :param db: str, database name
    :return: connection object
    """

    print('Establishing connection to MySQL')
    return MySQLdb.connect(host=host,
                           user=user,
                           passwd=pwd,
                           db=db)



# Close the connection to the database
def close_connection(conn):
    """
    Closes the connection to a database.

    :param conn: connection object
    """

    conn.close()



# Read data from MySQL table
def read_table(conn,
