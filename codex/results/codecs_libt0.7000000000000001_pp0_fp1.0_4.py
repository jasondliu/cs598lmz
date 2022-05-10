import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#'数据库地址'
HOSTNAME = '127.0.0.1'

#'数据库端口'
PORT = '3306'

#'数据库名'
DATABASE = 'mac'

#'数据库用户名'
USERNAME = 'root'

#'数据库密码'
PASSWORD = '123456'

#'数据库编码'
CHARSET = 'utf8mb4'

DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset={}'.format(
    USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE,CHARSET
)
SQLALCHEMY_DAT
