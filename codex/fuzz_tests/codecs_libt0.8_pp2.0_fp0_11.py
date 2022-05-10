import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


def init_db():
    db.create_all()



# def create_app(app_name, config=None, blueprints=None):
#     app = Flask(app_name)
#     register_blueprints(app, blueprints or None)
#     register_config(app, config or None)
#     db.init_app(app)
#     with app.app_context():
#         init_db()
#     return app


def register_config(app, config_module):
    app.config.from_object(config_module)


def register_blueprints(app, blueprints=None):
    if blueprints:
        for blueprint in blueprints:
            app.register_blueprint(blueprint)


@babel.localeselector
def get_locale():
    override = request.args.get('lang')

    if override:
        session['lang'] = override

    return session.get('lang',
