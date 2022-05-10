import selectors
import math
import re

sel = selectors.DefaultSelector()
host = 'www.baidu.com'
# url = '/'

# 
# request = 'GET %s HTTP/1.0\r\nHost: %s\r\n\r\n'

# 根据页面元素列表获取总页数
def getTotalPages(soup):
    pages = int(soup.select('div[class="pager"] > span[class="pager-list"] > a:nth-of-type(3)')[0].get_text())
    return pages

def getPerPageNum(soup):
    perPageNum = int(soup.select('div[class="pager"] > span[id="J_res_count"]')[0].get_text())
    return perPageNum

def getPageNumByRequest(content):
    soup = BeautifulSoup(content, 'html.parser')
