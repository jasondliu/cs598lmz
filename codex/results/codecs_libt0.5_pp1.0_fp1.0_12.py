import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'flask_mysql'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

# conn = mysql.connect()
# cursor = conn.cursor()

conn = pymysql.connect(host='localhost', user='root', password='root', db='flask_mysql',charset='utf8mb4')
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.
