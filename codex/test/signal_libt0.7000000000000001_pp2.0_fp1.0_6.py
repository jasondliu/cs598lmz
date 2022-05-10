import signal
signal.signal(signal.SIGINT, signal_handler)

# Connect to the database
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="sensors")        # name of the data base

# Create a cursor object
cursor = db.cursor()

# Create table as per requirement
# sql = """CREATE TABLE SENSORS (
#          TEMP  INT NOT NULL,
#          HUMIDITY INT NOT NULL)"""
# cursor.execute(sql)

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO SENSORS(TEMP,
         HUMIDITY)
         VALUES (%d,%d)""" % (temp, humidity)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

