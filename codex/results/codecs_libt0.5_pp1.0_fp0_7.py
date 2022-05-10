import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库连接
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test?charset=utf8mb4')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 添加到session:
# session.add(new_user)

# 提交即保存到数据库:
# session.commit()

# 关闭session:
# session.close()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如
