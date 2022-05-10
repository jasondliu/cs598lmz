import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import mysql.connector
from mysql.connector import errorcode

# Connect to the database
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='tweet_db')
cursor = cnx.cursor()

# Create a new table
TABLES = {}
TABLES['tweets'] = (
    "CREATE TABLE `tweets` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tweet_id` bigint(20) NOT NULL,"
    "  `text` varchar(150) NOT NULL,"
    "  `user_id` bigint(20) NOT NULL,"
    "  `user_screen_name` varchar(15) NOT NULL,"
    "  `user_name` varchar(30) NOT NULL,"
    "  `user_created_at` datetime NOT
