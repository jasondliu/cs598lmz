import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
