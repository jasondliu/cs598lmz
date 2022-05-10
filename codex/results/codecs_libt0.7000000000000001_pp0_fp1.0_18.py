import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from lxml import etree
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from lianjia.items import LianjiaItem


class LianjiaSpider(CrawlSpider):
	name = 'lianjia'
	allowed_domains = ["lianjia.com"]
	start_urls = [
	"http://esf.sh.fang.com/house/",
	]
	rules = (
		# Extract links matching 'category.php' (but not matching 'subsection.php')
		# and follow links from them (since no callback means follow=True by default).
		Rule(SgmlLinkExtractor(allow=('/house/[a-z]+/pg\d+/', )), callback
