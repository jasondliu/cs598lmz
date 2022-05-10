import codecs
codecs.register_error('strict', codecs.ignore_errors)

from werkzeug.contrib.fixers import ProxyFix
from flaskext.babel import Babel
from flask.ext.assets import Environment, Bundle

from momentjs import momentjs
from config import DefaultConfig
from .extensions import (db, cache, login_manager, admin, moment,
                         babel, mail, csrf, ckeditor)
from .views import frontend, account
from .views.open import open_bp
from .models import User, Post, Category, Tag, Comment
from .admin import CustomView, CustomModelView, CustomFileAdmin
from .utils import APP_DIR, INSTANCE_FOLDER_PATH


class ReverseProxied(object):
    '''Wrap the application in this middleware and configure the
    front-end server to add these headers, to let you quietly bind
    this to a URL other than / and to an HTTP scheme that is
    different than what is used locally.

    In nginx:
    location /myprefix {
        proxy_pass http://192.168.0.1:
