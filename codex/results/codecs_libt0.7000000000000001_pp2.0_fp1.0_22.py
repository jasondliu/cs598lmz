import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/movie'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/movie'

#初始化数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 是否追踪数据库的修改
# 生成加密实例
app.config["SECRET_KEY"] = "sadasdafsasddf"
#
