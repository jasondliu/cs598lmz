import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 定义爬虫
class Spider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        # 提取所有的段子
        duanzidivs = response.xpath('//div[@id="content-left"]/div')
        for duanzidiv in duanzidivs:
            # 分别处理每个段子
            author = duanzidiv.xpath('.//h2/text()').get().strip()
            content = duanzidiv.xpath('.//div[@class="content"]/span/text()').getall()
            content = ''.join(content).strip()
