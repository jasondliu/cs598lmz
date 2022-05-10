import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def fetch_data(url):
    """
    抓取数据
    """
    result = []
    r = requests.get(url)
    # print r.content
    # exit()
    soup = BeautifulSoup(r.content, 'html.parser')
    # print soup.prettify()
    # exit()
    table_list = soup.find_all('table', class_='tablelist')
    # print table_list
    # exit()
    for table in table_list:
        tr_list = table.find_all('tr')
        for index, tr in enumerate(tr_list):
            if index > 0:
                td_list = tr.find_all('td')
                if td_list:
                    temp_dict = dict()
                    temp_dict['company_name'] = td_list[0].a.text.strip()
                    temp_dict['company_addr'] = td_list
