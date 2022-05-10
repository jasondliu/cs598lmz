import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# --- Flask settings --- #

# Load Flask settings from config file
try:
    app.config.from_object('config')
except RuntimeError:
    print('Config file not found. Using default settings.')

# --- SQLAlchemy settings --- #

# Load SQLAlchemy settings from config file
try:
    app.config.from_object('config')
except RuntimeError:
    print('SQLAlchemy settings not found. Using default settings.')

# Create database engine using settings from config file
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Create database session
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

# --- Flask-Login settings --- #

# Create user loader function
@login_manager.user_loader
def load_user(user_id):
    try:
        user = session.query(User).filter_by(id=user_
