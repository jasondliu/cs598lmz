import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = 'CREATE TABLE IF NOT EXISTS `tieba` (' \
      '`id` bigint(20) NOT NULL AUTO_INCREMENT,' \
      '`title` varchar(255) DEFAULT NULL,' \
      '`href` varchar(255) DEFAULT NULL,' \
      '`author` varchar(255) DEFAULT NULL,' \
      '`create_time` varchar(255) DEFAULT NULL,' \
      '`reply_num` int(11) DEFAULT NULL,' \
      '`content` text,' \
      'PRIMARY KEY (`
