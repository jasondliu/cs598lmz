import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Define your own configurations by changing key value.
MYSQL_HOST     = "localhost"
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "*****"
MYSQL_DB_NAME  = "WenXueDB"


# Join path of system.
def get_absolute_path(path):
    return os.path.join(os.path.dirname(__file__), path)
