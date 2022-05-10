import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 获取页面内容
def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

# 解析索引页
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data
