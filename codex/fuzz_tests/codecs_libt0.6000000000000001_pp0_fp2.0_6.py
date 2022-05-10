import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# 配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 连接数据库
db = pymysql.connect(host=config['database']['host'],
                     port=int(config['database']['port']),
                     user=config['database']['user'],
                     password=config['database']['password'],
                     charset=config['database']['charset'],
                     db=config['database']['db'])
cursor = db.cursor()

# 打开浏览器
browser = webdriver.Chrome(executable_path=config['chrome']['executable_path'])

# 登录
browser.get(config['login']['url'])
browser.find_element_by_id(config['login']['
