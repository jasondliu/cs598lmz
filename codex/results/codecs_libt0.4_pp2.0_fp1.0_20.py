import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_db():
    if not hasattr(g, 'mysql_db'):
        g.mysql_db = connect_db()
    return g.mysql_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'mysql_db'):
        g.mysql_db.close()

def connect_db():
    return MySQLdb.connect(host=app.config['MYSQL_HOST'],
                           user=app.config['MYSQL_USER'],
                           passwd=app.config['MYSQL_PASSWORD'],
                           db=app.config['MYSQL_DB'],
                           charset='utf8mb4')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if
