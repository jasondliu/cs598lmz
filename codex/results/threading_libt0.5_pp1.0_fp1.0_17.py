import threading
threading.stack_size(1024 * 1024 * 512)

from . import app
from . import config
from . import db
from . import log
from . import models
from . import routes
from . import utils
from . import tasks
from . import jobs
from . import errors

from .models import User, Role, Permission, AnonymousUser, db_session
from .jobs import scheduler
from .tasks import celery

from flask_login import LoginManager
from flask_principal import Principal, Permission, RoleNeed
from flask_cors import CORS
from flask_migrate import Migrate

from flask_mail import Mail, Message
from flask_mail import mail

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import CSRFError

from flask_bcrypt import Bcrypt
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
from flask_bcrypt import current_app
from flask_bcrypt
