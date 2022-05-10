import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 爬取网页
def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
    html = requests.get(url, headers=headers)
    return html.text

# 获取网页内容
def getContent(html):
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, "html.parser")
    # 定位到段子所在的p标签
    content = soup.find_all('div', class_="post_item_body")
    # 使用for循环遍历
