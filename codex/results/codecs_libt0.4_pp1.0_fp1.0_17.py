import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Set up MySQL connection.
mysql = MySQLConnector(app, 'mydb')

# Set up Flask-Mail
mail = Mail(app)

# Set up Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Set up Flask-WTF
app.config['SECRET_KEY'] = 'KeepItSecretKeepItSafe'

# Set up Flask-Uploads
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# Set up Flask-Migrate
migrate = Migrate(app, mysql)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Set up Flask-Uploads
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# Set up Flask-Migrate
migrate = Migrate(app, mysql)
manager = Manager(app)
manager.add_command('db', MigrateCommand
