import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Configure to use MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db = SQLAlchemy(app)

# Import the models
from models import *

# Import the views
from views import *

# Import the API
from api import *

# Import the admin
from admin import *

# Import the admin
from admin_api import *

# Import the admin
from admin_api_v2 import *

# Import the admin
from admin_api_v3 import *

# Import the admin
from admin_api_v4 import *

# Import the admin
from admin_api_v5 import *

# Import the admin
from admin_api_v6 import *

# Import the admin
from
