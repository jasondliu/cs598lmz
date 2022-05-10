import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 使用pymysql 代替 MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

# 初始化数据库连接:
engine = create_engine('mysql://root:root@localhost:3306/test?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter
