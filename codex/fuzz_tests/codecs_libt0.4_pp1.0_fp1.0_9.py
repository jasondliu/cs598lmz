import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# create a Flask application - this ``app`` object will be used to handle
# inbound requests, routing them to the proper 'view' functions, etc
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SESSION_TYPE'] = 'filesystem'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()

# If you wanted to create a new database instead of using an existing one,
# create
