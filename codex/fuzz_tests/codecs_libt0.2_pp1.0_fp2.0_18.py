import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 创建爬虫
class ArticleSpider(scrapy.Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
                  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: " + title)
       
