import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Setting encoding
reload(sys)
sys.setdefaultencoding('utf-8')

# Creating SQLAlchemy base and engine
Base = declarative_base()
engine = create_engine("mysql://root:@127.0.0.1:3306/asylum_development"
                       , echo=False
                       , pool_recycle=3600)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Creating CSRF Form
class SearchForm(Form):
    search_str = TextField("search_str")

#Creating app object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'development-key'

#routes

@app.route("/")
def home():
    form = SearchForm(request.form) 
    return render_template("index.html",form=form)

@app.route("/search
