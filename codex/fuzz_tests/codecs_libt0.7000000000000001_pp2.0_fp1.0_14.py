import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# create_engine, 数据库连接
# echo = True, 会显示执行的SQL语句
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/new_ichunt?charset=utf8mb4', echo=True)

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(User).filter(User.
