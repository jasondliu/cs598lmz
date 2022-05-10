import codecs
codecs.register_error('ignore', codecs.lookup_error('ignore'))

# 解析网页
def parseHtml(html, url):
    soup = BeautifulSoup(html, 'lxml')
    # 标题
    title = soup.select_one('h1.title').get_text()
    # 正文
    content = soup.select_one('div.content').get_text()
    # 发布时间
    pubtime = soup.select_one('div.info').get_text()
    # 图片
    image = soup.select_one('div.content')
    image = image.find('img').get('src')
    # 相关文章
    related = soup.select('div.xg_left_480 > ul > li > a')
    related = [(rel.get_text(), rel.get('href')) for rel in related]

    return {
        'title': title,
        'content': content,
        'pubtime':
