import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_url(url):
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8')
    except:
        html = urllib.request.urlopen(url).read().decode('gbk')
    return html

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    div_list = soup.find_all('div', class_='list_item')
    for i in range(len(div_list)):
        div_list[i] = str(div_list[i])
    return div_list

def get_info(div_list):
    info_list = []
    for item in div_list:
        info = {}
        soup_item = BeautifulSoup(item, 'html.parser')
        info['title'] = soup_item.find('div', class_='list_title').get_text().strip()
        info['link'] = soup_item.find('div', class_='
