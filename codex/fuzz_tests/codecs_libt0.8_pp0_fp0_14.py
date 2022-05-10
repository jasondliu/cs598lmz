import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf-8mb4' else None)

# export DISABLE_SQLALCHEMY_TRACK_MODIFICATIONS=1
# sudo kill -9 `sudo lsof -t -i:5000`

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['UPLOAD_FOLDER'] = '/home/ubuntu/restserver/uploaded/'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
CORS(app)

# Elastic Beanstalk initalization
application = app

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'inventorydb'
app.config['MYSQL_DATABASE_HOST'] = 'inventorydb.cug
