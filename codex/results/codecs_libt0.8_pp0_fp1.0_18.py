import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/movies'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://movie_user:movie_user@10.0.0.16:3306/movies'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://movie_user:movie_user@127.0.0.1:3306/movie'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'asdfasdfasdf'

USER_FILES_DIR = 'static/user_files'

# 开启JSON自动序列化
JSON_AS_ASCII = False
#
# # app.config.from_envvar('FLASK_CONFIG')
#
# # app
