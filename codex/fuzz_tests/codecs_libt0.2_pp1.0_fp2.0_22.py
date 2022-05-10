import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='test', port=3306, charset='utf8')
cursor = conn.cursor()

# 创建表
sql = """CREATE TABLE IF NOT EXISTS `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""
cursor.execute(sql)

# 插入数据
sql = "INSERT INTO `test` (`name`, `age`) VALUES (%s, %s)"
cursor.execute(sql, ('
