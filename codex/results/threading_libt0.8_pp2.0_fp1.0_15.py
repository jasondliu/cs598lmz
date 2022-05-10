import threading
threading.stack_size(200*1024)  # set thread stack size

from spider import *
from worker import *
from schedule import *

#---------------------

class Job(object):
    """
    Job class that store all the relevant settings for the crawling tasks
    """
    def __init__(self, url, keyword, max_depth=3, timeout=30, max_crawl=10):
        self.url = url
        self.max_depth = max_depth
        self.timeout = timeout
        self.max_crawl = max_crawl
        self.keyword = keyword
        self.items = []
        self.result = {}   # key: url, value: list of items

    def run(self):
        """
        Execute the crawling job
        """
        max_thread = 20
        schedule = Scheduler(self.max_crawl)
        spider = Spider(self.keyword, self.max_depth, self.max_crawl)
        spider.setSchedule(schedule)

        # Start schedule
        schedule.run()

        # Start
