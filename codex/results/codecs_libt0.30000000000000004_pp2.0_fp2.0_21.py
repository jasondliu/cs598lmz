import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# mail = Mail(app)
# app.config.update(
#     MAIL_SERVER='smtp.qq.com',
#     MAIL_PROT=465,
#     MAIL_USE_TLS=True,
#     MAIL_USERNAME='25174727@qq.com',
#     MAIL_PASSWORD='wqwqwqwq'
# )
# mail
