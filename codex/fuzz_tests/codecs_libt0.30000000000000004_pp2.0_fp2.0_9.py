import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# create a Flask app
app = Flask(__name__)

# create a Flask-SQLAlchemy object
db = SQLAlchemy(app)

# create a Flask-WTF object
csrf = CSRFProtect(app)

# create a Flask-Login object
login_manager = LoginManager()
login_manager.init_app(app)

# load configuration from config.py
app.config.from_object('config')

# create a database connection object
db_uri = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4' % (
    app.config['DB_USERNAME'],
    app.config['DB_PASSWORD'],
    app.config['DB_HOST'],
    app.config['DB_PORT'],
    app.config['DB_NAME']
)
app.config['SQLALCHEMY_DATABASE_
