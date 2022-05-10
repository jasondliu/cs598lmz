import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# CONFIGURATION
HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "root"
DATABASE = "chris-dashboard"

# if setting up with docker-compose, use mysql service name: DATABASE_URL="mysql://root:root@mysql:3306/chris-dashboard"
DATABASE_URL = "mysql://{}:{}@{}:{}/{}".format(USER, PASSWORD, HOST, PORT, DATABASE)

# Init app
app = dash.Dash(
    __name__,
    external_stylesheets=[
        "//cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css",
        "//fonts.googleapis.com/css?family=Roboto+Mono:500|Raleway:300,400,500
