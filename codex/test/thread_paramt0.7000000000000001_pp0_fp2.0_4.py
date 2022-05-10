import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def get_html(url):
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_link(url):
    html = get_html(url)
    soup = BeautifulSoup(html)
    #title = soup.find(text='相关搜索：').find_parent('div').find('a')
    title = soup.find('div', id='res-topinfo').find('a')
    if title is not None:
        return title['href']
    return ''

def get_info(url):
    html = get_html(url)
    soup = BeautifulSoup(html)
    title = soup.find('div', id='res-topinfo').find('h3').text.strip()
    detail = soup.find('div', id='res-detailinfo').find_all('p')
