import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

#初始化数据库连接
engine = create_engine('mysql+mysqldb://root:root@localhost:3306/scrapy?charset=utf8mb4')
#创建DBSession类型
DBSession = sessionmaker(bind=engine)

#创建session对象
session = DBSession()

#创建新User对象
new_user = User(id='5',name='Bob')
#添加到session
session.add(new_user)
#提交即保存到数据库
session.commit()
#关闭session
session.close()
