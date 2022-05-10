import codecs
codecs.register_error('strict', codecs.ignore_errors)

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from scrapy.http import Request
from scrapy.selector import Selector

from amazonmws import django_cli
django_cli.execute()

from amazonmws import utils as amazonmws_utils
from amazonmws.loggers import GrayLogger as logger, StaticFieldFilter, get_logger_name
from amazonmws.model_managers import *


class AmazonBestSellersSpider(scrapy.Spider):
    name = "amazon_best_sellers"

    __allowed_category_ids = [
        # "165793011", # Beauty
        # "16310101", # Clothing
        # "11055981", # Handmade
        # "13900851", # Health
        # "1036592", # Home
        "3760911", # Industrial
        # "16310091", # Jewelry
        # "297
