import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import mysql.connector
from mysql.connector import errorcode

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mysql',
                              charset='utf8mb4',
                              use_unicode=True)
cursor = cnx.cursor()

# Create a new database named 'employees'
DB_NAME = 'employees'

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F')
