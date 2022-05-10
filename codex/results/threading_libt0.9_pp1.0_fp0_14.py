import threading
threading.stack_size(1024)*1024

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    # crud
    mongo.init_app(app)
    # user_auth.init_app(app)
    # assets.init_app(app)
    # Generate login_manager and load related config
    login_manager.init_app(app)
    login_manager.login_view = 'signin'

    from . import auth
    from . import instagram

    app.register_blueprint(auth.bp)
    app.register_blueprint(instagram.bp)
    app.add_url_rule('/', endpoint='index')

    return app


app = create_app()
