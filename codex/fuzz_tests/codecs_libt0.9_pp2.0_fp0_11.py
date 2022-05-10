import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app=Flask(__name__)#创建flask实例
app.config.from_object('config')#导入配置文件


# 连接到MySQL数据库需要进行导入模块
# 如果机器上已经安装了mysqlclient，就使用mysqlclient
# 如果机器上没有安装mysqlclient，就使用pymysql，pymysql没有安装就会把它自动进行安装
try:
    from .mysql import MySQL
except:
    from .pymysql import MySQL


#
