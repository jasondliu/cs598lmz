import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

config = {
    'host': 'localhost',
    'user': 'dbuser',
    'password': '123456',
    'db': 'web',
    'charset': 'utf8mb4',
    'port': 3306
}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'harda to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dbuser:123456@localhost/web'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment(app)
db = SQLAlchemy(app)

#migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
manager = Manager
