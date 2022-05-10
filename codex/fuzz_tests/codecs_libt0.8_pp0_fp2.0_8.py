import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

app = Flask(__name__)

# Database Server Information
db_host = 'localhost'
db_port = '3306'
db_user = 'root'
db_passwd = 'mysql'
db_name = 'CSE455'

# Connect to the server and select the database
def connect_db():
	db = pymysql.connect(db_host, db_user, db_passwd, db_name)
	db_cursor = db.cursor()
	return db, db_cursor

# Close the connection to the database
def close_db(db, db_cursor):
	db.close()
	db_cursor.close()

# Convert dimentions from inches to meters
def inch_to_meter(num):
	return num*0.0254

def meter_to_inch(num):
	return num/0.0254

# Convert a list of patient information to json
def patient
