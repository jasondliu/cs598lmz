import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# from .views import *

def run_server():
    app = Flask(__name__)

    app.config.update(
        SECRET_KEY = 'P@ssw0rd!',
        DEBUG = True,
        TEMPLATES_AUTO_RELOAD = True,
        SESSION_COOKIE_SECURE = False,
        SESSION_COOKIE_HTTPONLY = True
    )

    app.config['SESSION_TYPE'] = 'filesystem'
    sess = Session()
    sess.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():

        if request.method == 'POST':
            username = request.form.get('username', None)
            password = request.form.get('password', None)

            if username
