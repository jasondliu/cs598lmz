import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#抓取新闻标题
def getNewsTitle(newsUrl):
    res = requests.get(newsUrl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    news_title = soup.select('.main-title')[0].text
    return news_title

#抓取新闻内容
def getNewsContent(newsUrl):
    res = requests.get(newsUrl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    news_content = soup.select('#artibody')[0].text.replace('\n', '').replace('\u3000', '')
    return news_content

#抓取新闻发布时间
def getNewsTime(newsUrl):
   
