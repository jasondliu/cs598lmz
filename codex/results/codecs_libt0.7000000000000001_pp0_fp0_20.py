import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    db.init_app(app)
    # login_manager.init_app(app)
    # login_manager.login_view = 'auth.login'

    # register the database commands
    from project.api import models
    from project.api import auth
    from project.api import user_api
    from project.api import common_api

    app.register_blueprint(auth.auth_blueprint)
    app.register_blueprint(user_api.user_blueprint)
    app.register_blueprint(common_api.common_blueprint)
    return app
