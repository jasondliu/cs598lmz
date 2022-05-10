import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(filename='app.log',format='[%(asctime)s] %(levelname)s: %(message)s',level=logging.INFO)

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/test?charset=utf8mb4'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
app.config['SQLALCHEMY
