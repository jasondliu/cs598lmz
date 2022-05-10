import codecs
codecs.register_error('ignore_tags', codecs.ignore_errors)

config = ConfigObj('config/site.ini')

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=config['generic']['secret_key'],
    DATABASE=os.path.join(app.instance_path, '_db.sqlite'),
)
app.debug = True
app.host = '0.0.0.0'
app.port = 8000

if not os.path.exists(app.instance_path):
    os.makedirs(app.instance_path)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/articles/')
def articles():
    db = sqlite3.connect(
        app.config['DATABASE'],
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    db.row_factory = sqlite3.Row

    articles = db.execute(
        'SELECT id, created
