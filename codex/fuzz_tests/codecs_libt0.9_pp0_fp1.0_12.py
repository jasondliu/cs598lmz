import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda')

#SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///blog?instance=inspiring-albattani-819:inspiring-albattani-819'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:123456@localhost/blog'
#SQLALCHEMY_BINDS = {'blog': SQLALCHEMY_DATABASE_URI}

app.config.from_object(__name__)
db = SQLAlchemy(
