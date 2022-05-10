import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 定义一个类，用来保存解析出来的信息
class Movie(object):
    def __init__(self):
        self.name = ''
        self.year = 0
        self.score = 0
        self.director = ''
        self.classification = ''
        self.actor = ''

# 定义一个函数，用来从电影详情页面解析出电影信息
def get_movie_info(url):
    # 创建一个movie对象
    movie = Movie()
    # 获取电影详情页面的内容
    html = get_one_page(url)

