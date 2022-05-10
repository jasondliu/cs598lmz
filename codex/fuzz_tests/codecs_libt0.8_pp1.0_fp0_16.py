import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@127.0.0.1:3306/my_blog?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS=True

SECRET_KEY='123456'
CSRF_ENABLED=True

# MAIL_SERVER = ''
# MAIL_PORT = 25
# MAIL_USE_TLS = False
# MAIL_USE_SSL = False
# MAIL_USERNAME = 'XXXX@XXX.com'
# MAIL_PASSWORD = 'XXXX'
