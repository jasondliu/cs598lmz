import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# For MySQL
import MySQLdb

# For PostgreSQL
import psycopg2

# For MSSQL
import pymssql

# For Oracle
import cx_Oracle

# For MongoDB
from pymongo import MongoClient

# For Redis
import redis

# For Elasticsearch
from elasticsearch import Elasticsearch


class DatabaseConnection(object):
    """
    This class is a generic class which can be used to connect to any database
    """

    def __init__(self, db_type, db_host, db_port, db_user, db_pass, db_name):
        self.db_type = db_type
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name

    def connect(self):
        """
        This function is used to
