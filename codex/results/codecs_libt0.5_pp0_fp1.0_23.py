import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='mysql',
    charset='utf8mb4'
)
cur = conn.cursor()
cur.execute('USE scraping')

# 抓取百度百科python页面上的链接
def scrape_baidu_baike_python():
    url = 'https://baike.baidu.com/item/Python/407313'
    html = download(url)
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    content = soup.find('div', id='content')
    print(content)
    links = content.find_all('a')
    print(links)
    for link
