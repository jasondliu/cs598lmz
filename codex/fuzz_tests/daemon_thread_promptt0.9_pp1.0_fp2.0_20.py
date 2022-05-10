import threading
# Test threading daemon
t = threading.Thread(target=socketio.run,'127.0.0.1',5000)
t.daemon = True
t.start()

app = Flask(__name__)

@app.before_request
def _db_connect():
	db = connection.connect_to_database()
	db.connect()

@app.teardown_request
def _db_close(exc):
	if not db.is_closed():
		db.close()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login/', methods=['POST'])
def login():
	ukey = request.args.get('key')
	if check_access_key(ukey):
		return jsonify({"error": 0, "message": "Authenticated"})
	else:
		return jsonify({"error": 1, "message": "You are not authorized"})

@app.route('/search/', methods=['POST'])
def search():
	u
