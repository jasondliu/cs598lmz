import ctypes
ctypes.cast(None, ctypes.py_object)
import sys

# Flask
application = Flask(__name__)

# Bootstrap
Bootstrap(application)


# Flask-MongoEngine
application.config['MONGODB_SETTINGS'] = {
    'db': 'fridgit',
    'host': 'mongodb://localhost:27017/',
    'username': 'admin',
    'password': 'admin',
}

db = MongoEngine(application)

## JWT
application.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(application)


# Flask-Login
login_manager = LoginManager()
login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.objects.get(user_id)

@application.before_first_request
def load_languages():
    with open('languages.json', 'r') as infile:
       
