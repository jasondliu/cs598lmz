import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../config/db.json')
# db_config = json.load(open(path))
# dburl = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
#     db_config['user'], db_config['password'], db_config['host'], db_config['port'], db_config['schema'])
# app.config['SQLALCHEMY_DATABASE_URI'] = dburl
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)

