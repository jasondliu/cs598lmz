import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.debug = False
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "This is the default index"


@app.route('/users', methods=['GET'])
def get_users():
    """
    Returns a list of users
    """
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/user', methods=['GET'])
def get_user():
    """
    Returns a list of users
    """
    conn = mysql
