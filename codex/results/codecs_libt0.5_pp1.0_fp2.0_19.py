import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 设置日志
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)

# 导入Flask
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

# 导入扩展
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask_migrate import Migrate, MigrateCommand
migrate = Migrate(app, db)

from flask_script import Manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

