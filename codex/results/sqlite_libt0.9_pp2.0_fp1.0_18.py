import ctypes
import ctypes.util
import threading
import sqlite3

#parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-source_db')
parser.add_argument('-dest_db')
parser.add_argument('-username')
parser.add_argument('-password')
args = parser.parse_args()

#hard code a start date and an end date, must be in the range[‘1999-01-01’, ‘2018-12-31’] inclusive
start_date = '2017-11-16'
end_date = '2017-12-16'

#endpoint for web service calls
endpoint = 'http://ec2-54-85-105-244.compute-1.amazonaws.com/api/v1'

#get all the user IDs from the source database
db_connection = sqlite3.connect(args.source_db)
db_cursor = db_connection.cursor()
db_cursor.execute("SELECT DISTINCT user FROM triplog WHERE start_date >= ? AND end_date <= ?", [start_date,end
