import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    app.jinja_env.add_extension('jinja2.ext.with_')
    app.jinja_env.add_extension('jinja2.ext.do')

    if app.config['DEBUG']:
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)

    from .database import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import views
    from .api import api
    from .auth import auth
    from .admin import admin
    app.register_blueprint(views
