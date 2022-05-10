import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# create a Flask application
app = Flask(__name__)

# tell Flask to use this specific template engine to render the templates
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# turn off the verbose messages from PyJade
app.jinja_env.pyjade.options['pretty'] = False

# add the static file directory
# static_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
# print static_folder
app.static_folder = 'static'
# print app.static_folder

# initialize the database
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'exam'
app.
