import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/douban_book_db?charset=utf8mb4')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 1. 创建新User对象:
new_user = Book(name='Python编程',author='作者',score=9.4)
# 2. 添加到session:
session.add(new_user)
# 3. 提交即保存到数据库:
session.commit()

# 关闭session:
session.close()
