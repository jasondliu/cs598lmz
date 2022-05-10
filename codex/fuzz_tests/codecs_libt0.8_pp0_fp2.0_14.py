import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def init(app):
    #app.app_context().push()
    db.init_app(app)
