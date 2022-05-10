import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 生成一个app实例
app = Flask(__name__)
app.config.from_pyfile('app.conf')
# 加载配置文件内容
db = SQLAlchemy(app)
# 初始化数据库

# 定义模型
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)
    is_activated = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password, is
