import codecs
codecs.register_error('ignore', codecs.lookup('utf-8'))

# For debugging
#for key, val in enumerate(sys.modules):
#    print(key, val)

# Import our modules
import gf
import gf_helpers
import gf_database

# Set up our main variables
gf_helpers.setup_vars()

# Set up our DB
if not gf_helpers.load_config():
    gf_helpers.setup_db()
    gf_helpers.setup_config()

# Set up our database
db = gf_database.gf_database()
db.connect()

# Set up our API
app = gf.app
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + gf.db_file
app.config['SQLALCHEMY_ECHO'] = False

# Set up our API
api
