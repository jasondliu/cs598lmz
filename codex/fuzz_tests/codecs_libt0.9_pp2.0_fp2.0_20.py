import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def scrape():
    buttons = []
    s_list = []

    browser = webdriver.Chrome('C:/Users/win/Downloads/chromedriver.exe')
    url = "https://www1.president.go.kr/petitions"
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    bs = BeautifulSoup(html, 'html.parser')

    ul_list = bs.select('ul>li>a')
    for i in ul_list:
        if i.text == '[전체]': i.text = 'All'
        buttons.append(i.text)
    for i in range(1, len(buttons)):

        lists = Chrome_select('#cont_view > div.cs_area > div.board.text > div > div.board_footer > div.btn_group > button:nth-child(2)', browser)
