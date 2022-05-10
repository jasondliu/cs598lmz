import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建一个数据库连接
conn = pymysql.connect(host='localhost', user='root', passwd='', db='test', charset='utf8mb4')

# 创建一个游标
cursor = conn.cursor()

# 创建一个表
sql = '''
    CREATE TABLE IF NOT EXISTS `users` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `email` varchar(255) COLLATE utf8_bin NOT NULL,
      `password` varchar(255) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    AUTO_INCREMENT=1 ;

