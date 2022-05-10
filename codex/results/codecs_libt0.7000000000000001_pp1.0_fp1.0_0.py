import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql = MySQL(app)


@app.route('/')
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM items''')
    rv = cur.fetchall()
    return str(rv)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/test')
# def test():
#     return 'test'


if __name__ == '__main__':
    app.
