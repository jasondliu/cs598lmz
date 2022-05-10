import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库连接
def get_db_conn():
    db_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '123456',
        'db': 'test',
        'charset': 'utf8mb4'
    }
    conn = MySQLdb.connect(**db_config)
    return conn

# 创建表
def create_table():
    conn = get_db_conn()
    cursor = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS `test`(
      `id` INT UNSIGNED AUTO_INCREMENT,
      `name` VARCHAR(100) NOT NULL,
      `age` TINYINT UNSIGNED NOT NULL,
      `sex` ENUM('男', '女')
