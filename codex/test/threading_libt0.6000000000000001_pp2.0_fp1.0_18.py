import threading
threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)

# 这个函数是我们的爬虫
def spider(url):
    time.sleep(random.random())
    res = requests.get(url)
    return res.text

# 这个函数是我们的解析器
def parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    my_girl = soup.find_all('img')
    return my_girl

# 这个函数是我们的存储器
def saver(girl):
    filename = girl.get('alt') + '.jpg'
    img = requests.get(girl.get('data-original'))
    f = open(filename, 'ab')
    f.write(img.content)
    f.close()

