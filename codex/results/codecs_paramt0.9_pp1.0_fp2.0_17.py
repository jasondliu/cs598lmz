import codecs
codecs.register_error('ignore_utf_8_errors', codecs.ignore_errors(u'utf8'))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secretkey'
app.config['CSRF_ENABLED'] = True
app.config['CSRF_SESSION_KEY'] = 'secretkey'

mongo = PyMongo(app, config_prefix='MONGO')
csrf = CSRFProtect(app)
#login = LoginManager()
#login.init_app(app)

#from app.views import index
#from app.views import stylesheet
#from app.views import bootstrap3
#from app.views import wysihtml_editor
#from app.views import signup
#from app.views import login
#from app.views import logout
#from app.views import dashboard
#from app.views import profile

#from app.view.form import form
from app.view.web import web
from app.lib.login_manager import login_manager

app.register_blue
