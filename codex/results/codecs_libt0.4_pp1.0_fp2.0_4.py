import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')

# Connect to DB
db = SQLAlchemy(app)

# Migrate
migrate = Migrate(app, db)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# OAuth
oauth = OAuth(app)

from models import *
from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0')
