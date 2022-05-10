import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 加载数据库配置
from config import *

# 初始化数据库连接:
engine = create_engine(
    'mysql+mysqldb://' + MYSQL_USER + ':' + MYSQL_PASSWORD + '@' + MYSQL_HOST + ':' + MYSQL_PORT + '/' + MYSQL_DB + '?charset=utf8mb4',
    echo=True,
    pool_recycle=3600)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 插入数据
new_user = User(id='5', name='Bob')
session.
