import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE wikipedia")

# 定义一个func，用来判断输入的词是否在数据库中
def pageRank(links, iterNum=20):
    # 创建一个字典，用来存储页面的PR值
    PR = dict()
    # 获取links中所有页面的名称
    pages = set(links.keys())
    # 获取links中所有
