import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.user_loader(load_user)
lm.login_view = 'login'
lm.setup_app(app)

def initilize_db():
    db.create_all()

initilize_db()

from app import views, models
