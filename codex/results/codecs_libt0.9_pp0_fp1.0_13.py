import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

LOG_FORMAT =   "%(asctime)s [%(levelname)s] %(message)s"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/zhihi'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 50
app.config['ELASTICSEARCH_INDEX'] = "zhihu"
app.config['ELASTICSEARCH_DOC_TYPE'] = "doc"
es = FlaskElasticsearch(app)

db = SQLAlchemy(app)
session = db.session

handler = RotatingFileHandler('/opt/log/zhihi-index.log', maxBytes=1024 * 1024 * 100, backupCount=10, encoding='UTF-8')  # 实
