import codecs
codecs.register_error('strict', codecs.ignore_errors)

###############################################################################

app = Flask(__name__)
app.secret_key = ''  # Set this

# Setup the database
engine = create_engine(os.environ.get('DATABASE_URL'))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

###############################################################################

# Set up the tables in the database

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(32))
    salt = Column(String(32))
    first_name = Column(String(32))
    last_name = Column(String(32))

    def __init__(self, username, password, first_name, last_name):

