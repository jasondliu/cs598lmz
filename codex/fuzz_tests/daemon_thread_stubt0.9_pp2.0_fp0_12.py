import sys, threading

def run():
    print(threading.currentThread().getName() + ' start')
    time.sleep(1)
    print(threading.currentThread().getName() + ' stop')

for i in range(1, 6, 1):
    t = threading.Thread(target=run, name='Thread '+str(i))
    t.start()

# 创建子线程
def get_detail_html(url):
    # 爬取文章详情
    response_detail = requests.get(url)
    detail_html = response_detail.content.decode("utf-8")
    return detail_html

# 获取文章详情url列表
def get_detail_url_list(url):
    # 请求文章列表页
    response = requests.get(url)
    #  取出文章列表页的html
    html = response.content.dec
