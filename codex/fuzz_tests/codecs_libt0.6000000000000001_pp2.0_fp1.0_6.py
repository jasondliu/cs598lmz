import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class PublicSpider(scrapy.Spider):
    name = "public"
    allowed_domains = ["news.sina.com.cn", "news.sohu.com", "news.163.com", "news.qq.com", "finance.sina.com.cn",
                       "finance.sohu.com", "finance.163.com", "finance.qq.com", "finance.ifeng.com",
                       "finance.eastmoney.com", "stock.stockstar.com", "stock.hexun.com", "stock.sohu.com",
                       "stock.eastmoney.com", "stock.eastmoney.com", "stock.ifeng.com", "stock.qq.com",
                       "stock.163.com", "stock.cfi.cn", "stock.caijing.com.cn", "www.yicai.com", "www.caixin.com",
                       "www.caijing.
