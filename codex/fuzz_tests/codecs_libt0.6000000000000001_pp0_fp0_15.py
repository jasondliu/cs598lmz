import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
def get_connect():
	connect = pymysql.connect(
		host = 'localhost',
		port = 3306,
		user = 'root',
		password = '123456',
		db = 'mydb',
		charset = 'utf8mb4'
	)
	return connect

# 创建表
def create_table():
	connect = get_connect()
	cursor = connect.cursor()
	sql = """create table user(
			id int primary key auto_increment,
			username varchar(20),
			password varchar(20),
			age int
			) charset=utf8mb4"""
	cursor.execute(sql)
	connect.close()

# 插入数据
def insert_data():

