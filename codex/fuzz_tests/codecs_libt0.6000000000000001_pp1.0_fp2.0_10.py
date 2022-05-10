import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connect
conn = pymysql.connect(host='localhost', user='root', password='', db='crawling', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = """insert into crawling.tour(title, content, img, link)
         values(%s, %s, %s, %s)"""

# Chrome Driver
driver = webdriver.Chrome("./chromedriver.exe")

# 여행지 정보 가져오기
def get_info():
    driver.get("https://www.tour.go.kr/main/index.tour")
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    data1 = soup.select("#contents > div.navi
