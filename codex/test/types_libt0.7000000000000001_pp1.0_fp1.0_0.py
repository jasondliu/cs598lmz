import types
types.ModuleType.__repr__ = lambda self: "<module '{0}'>".format(self.__name__)

def create_app():
    """Create an application instance."""

    # Create app
    app = Flask(__name__)

    # Load config
    app.config.from_object(__name__ + '.config')
    app.config.from_envvar('{}_SETTINGS'.format(__name__.upper()), silent=True)
    app.config.update(dict(
        DEBUG=os.environ.get('DEBUG', app.config.get('DEBUG', False)),
        HOST=os.environ.get('HOST', app.config.get('HOST', '127.0.0.1')),
        PORT=int(os.environ.get('PORT', app.config.get('PORT', 5000))),
    ))

