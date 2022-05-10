import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
# log日志的配置
log_level = config['log']['Level']
logger.setLevel(log_level)
formatter = logging.Formatter('%(asctime)s-%(filename)s-%(funcName)s-%(levelname)s-%(lineno)s-%(message)s')

# 读取redis配置
redis_host = config['redis']['host']
redis_port = config['redis']['port']
redis_db = config['redis']['db']
redis_password = config['redis']['password']

# 读取邮件配置
