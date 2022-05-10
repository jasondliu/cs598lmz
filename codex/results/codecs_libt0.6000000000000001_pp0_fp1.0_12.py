import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from database import *


@app.route('/')
@app.route('/index')
@app.route('/main')
def index():
    return 'Hello world!'

@app.route('/list')
def list():
    return jsonify(list(map(lambda x: x.to_dict(), User.query.all())))

if __name__ == '__main__':
    app.run(debug=True)
