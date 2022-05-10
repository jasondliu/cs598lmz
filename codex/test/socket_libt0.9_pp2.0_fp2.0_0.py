import socket

# Defining path related objects
HOST = socket.gethostname()
PORT = 4567
SECRET_KEY = os.urandom(24)

# Defining app object
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('DJAGOL_SETTINGS', silence=True)

# Load the views and models
import djagol.views, djagol.models
