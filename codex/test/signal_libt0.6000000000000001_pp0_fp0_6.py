import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Scrapy settings for xiaoqu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiaoqu'

SPIDER_MODULES = ['xiaoqu.spiders']
NEWSPIDER_MODULE = 'xiaoqu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
