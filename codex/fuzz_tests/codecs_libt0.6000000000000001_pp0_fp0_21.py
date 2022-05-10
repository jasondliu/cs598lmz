import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Initialize Flask application
app = Flask(__name__)

# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'secretkey'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '******'
app.config['MYSQL_DATABASE_DB'] = 'student'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# Define SQLAlchemy
db = SQLAlchemy(app)

# Initialize MySQL
mysql = MySQL(app)

# Define login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Define a User class
class User(flask_login.UserMixin):
   
