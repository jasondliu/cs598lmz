import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
db = pymysql.connect(host='localhost', user='root', password='root', db='test', charset='utf8mb4')
cursor = db.cursor()

# 创建数据库表
sql = '''
CREATE TABLE IF NOT EXISTS `test`.`test_table` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `age` INT NULL,
  `sex` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;
'''
cursor.execute(sql)

# 插入数据
sql = '''
