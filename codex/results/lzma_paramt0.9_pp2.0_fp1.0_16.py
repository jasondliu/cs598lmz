from lzma import LZMADecompressor
LZMADecompressor()


class ZenyHelper:
    def __init__(self, zeny_url):
        self.client = SlackClient(SLACK_TOKEN)
        self.zeny_url = zeny_url

    def get(self):
        url = self.naver_zeny_api_url()
        response = requests.get(url)
        html = response.text
        self.parse(html)

    def naver_zeny_api_url(self):
        return 'https://m.stock.naver.com/api/json/sise/dailySiseIndexListJson.nhn?code=%s&pageSize=50' %self.zeny_url

    def parse(self, html):
        html = lzma.decompress(html.encode('utf-8'))
        html = html.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        sise_index_json = json.loads(soup.text)
        yesterday = self.getYesterday()

        yesterday_index = self
