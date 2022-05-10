import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from flask_babel import gettext as _
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_uploads import patch_request_class
from flask_dropzone import Dropzone

from elasticsearch import Elasticsearch

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()

photos = UploadSet('photos', IMAGES)
dropzone = Dropzone()


def create_app
