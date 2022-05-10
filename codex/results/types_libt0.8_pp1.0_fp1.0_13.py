import types
types.ModuleType.__repr__ = types.ModuleType.__str__

config = ConfigParser(allow_no_value=True)
config.read(path.join(path.dirname(__file__), 'ini', 'pkgdb.ini'))

# Disable the cache while testing # FIXME: auto-clear cache
config.set('pkgdb', 'cache_url', 'null')

# Load ini configuration
pkgdb = Flask('pkgdb', template_folder='../templates')
pkgdb.config.from_object('ini.pkgdb')
pkgdb.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
pkgdb.url_map.converters['RegexConverter'] = RegexConverter


if 'DEBUG' in config.get('pkgdb', 'allowed_envs'):
    pkgdb.debug = True

if 'testing' in config.get('pkgdb', 'allowed_envs'):
    pkgdb.testing = True

# Set up the custom jinja environment.
pkgdb.jinja_env.
