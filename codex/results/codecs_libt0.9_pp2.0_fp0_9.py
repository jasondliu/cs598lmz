import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# 抓取西刺代理网页：
def get_ip_list(url):
    web_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text,'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1,len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text+':'+tds[2].text)
    return ip_list
# 抓取快代理网页：
def get_ip_list_kdaili(url):
    web_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(web_
