import threading
threading.stack_size(1024*1024)

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)

def worker(urls):
    for url in urls:
        try:
            fetch_url(url)
        except Exception, e:
            logging.error("ERROR: %s: %s" % (url, e))

def fetch_url(url):
    logging.info("Fetching %s" % url)
    rsp = urllib2.urlopen(url)
    result = rsp.read()
    logging.info("%s: %s" % (url, len(result)))

def main():
    urls = [
        "https://www.baidu.com/",
        "https://www.bing.com/",
        "https://www.sogou.com/",
        "https://www.so.com",
    ]
    thread_count = 2

