import threading
# Test threading daemon
import daemon
# Test memcache moduel
import memcache

import MySQLdb

def connect():
    """ Connect to MySQL database """

    try:
        conn = MySQLdb.connect(host   = DBHOST,
                               user   = DBUSER,
                               passwd = DBPASS,
                               db     = DB)
        return conn

    except MySQLdb.Error, e:
        return 'Error: %s' % e

def disconnect(conn):
    """ Disconnect from MySQL database """

    conn.close()

def update():
    """ Update values to MySQL database """

    # Create database connection
    conn = connect()

    # Create database cursor
    cursor = conn.cursor()

    # Update database values
    cursor.execute('UPDATE %s SET `db_value` = `db_value` + 1 WHERE `db_id` = 1' \
                   % (DBTABLE))

    # Close database cursor and commit changes
    cursor.close()

    # Close database connection
    disconnect(conn)

# Set database information
DBHOST = 'localhost'
DBUSER
