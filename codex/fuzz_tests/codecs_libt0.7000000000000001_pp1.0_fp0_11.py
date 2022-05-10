import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Creating the app and setting the config
app = Flask(__name__)
app.config.from_object('config')

# Creating a database instance
db = SQLAlchemy(app)

# Creating a Migrate instance
migrate = Migrate(app, db)

# Creating a login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Creating a mail instance
mail = Mail(app)

# Creating an instance of the white list
white_list = WhiteList(app)

# Creating an instance of the blacklist
black_list = BlackList(app)

# Creating an instance of the rsvp
rsvp = RSVP(app)

# Creating an instance of the invite
invite = Invite(app)

# Creating an instance of the contact
contact = Contact(app)

# Creating an instance of the mail
mail = Mail(app)

# Creating an instance of the mail_log
mail_
