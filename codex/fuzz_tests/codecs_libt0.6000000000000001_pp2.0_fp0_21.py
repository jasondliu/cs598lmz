import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
	return "Welcome to the Homepage!"

@app.route('/CreateUser/<username>/<password>')
def create_user(username, password):
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.callproc('spCreateUser', (username, password))
	data = cursor.fetchall()

	if len(data) is 0:
		conn.commit()
		return json.dumps({
