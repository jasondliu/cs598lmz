import ctypes
import ctypes.util
import threading
import sqlite3
import time
from datetime import datetime
import json
import uuid
import re
import os
import sys
from . import lib
from . import config
from . import utils
from . import pymysql
from . import sqlite3
from . import psycopg2
from . import cx_Oracle
from . import pymssql
from . import mysql
from . import postgresql
from . import oracle
from . import mssql

class Database(object):
    """
    Database object
    """
    def __init__(self, db_name, db_type, host, port, user, password, db_name_2 = None, db_type_2 = None, host_2 = None, port_2 = None, user_2 = None, password_2 = None):
        self.db_name = db_name
        self.db_type = db_type
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name_2 = db_name_2
        self
