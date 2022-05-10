import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connection
conn = pymysql.connect(host='localhost', user='root', password='', db='crawling', charset='utf8mb4')
c = conn.cursor()
print("MySQL Connection 연결 !")

# Crawling 함수 구현
def crawling(url):
    sourcecode = requests.get(url)
    plain_text = sourcecode.text
    soup = BeautifulSoup(plain_text, 'lxml')

    # 제목 크롤링
    for title in soup.select('h3 > a'):
        title_link = title.get('href')
        get_text = title.string
        print(get_text)

        # 내용 크롤링
        get_content = ''
        req = requests.get(title_link)
        plain_
