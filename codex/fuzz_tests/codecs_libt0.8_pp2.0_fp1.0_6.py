import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 查看系统编码
print sys.getdefaultencoding()

# 配置命令行方式运行网址
page = 'http://learnscrapy.com/page/'
# 爬取的页数
page_start = 1
page_stop = 2

# 初始化列表存储数据
items = []

# 爬虫开始爬取页面
for i in range(page_start,page_stop):
    url = page+str(i)+'/'
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html,"html.parser")

    #
