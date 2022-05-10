import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin.contrib.sqla import ModelView

# Flask-SQLAlchemy uses SQLAlchemy, which is an Object Relational Mapper (ORM)
# for Python. It lets you describe the database model using Python code.
db = SQLAlchemy()

# Flask-Migrate is an extension that handles SQLAlchemy database migrations for
# Flask applications using Alembic. The database operations are made available
# through the Flask command-line interface or through the Flask-Script extension.
migrate = Migrate()

# Flask-Admin is a Flask extension that lets you add admin interfaces to Flask
# applications.
admin = Admin(template_mode='bootstrap3')

class User(UserMixin, db.Model):
    """
