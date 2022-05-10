import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pv9HWy!Jp!j7!n3t'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+mysqlconnector://root:1@127.0.0.1:3306/web?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 初始化数据库
db = SQLAlchemy(app)

# 模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True
