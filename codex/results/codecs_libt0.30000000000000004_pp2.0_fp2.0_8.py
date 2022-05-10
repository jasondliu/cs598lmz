import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Set up database
engine = create_engine('mysql+mysqldb://root:@localhost:3306/{0}?charset=utf8mb4'.format(DB_NAME), pool_recycle=3600)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Set up Flask-User to handle user account related forms
user_manager = UserManager(app, db, User)

# Create 'close_db' function for use in Flask-User
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# Create customized index view class that handles login & registration
class MyIndexView(UserManager.UserManagerIndexView):
    @user_manager.unauthorized_handler
   
