import sys, threading

def run():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    url = 'https://shopee.co.id/search?keyword=sneakers'
    html = None
    while (html is None):
        try:
            response = requests.get(url, headers=headers)
            html = response.text
        except:
            print('Calm down donk!')
            pass
    res = BeautifulSoup(html, 'html.parser')
    res = res.findAll('span',{'class':'_1w9jLI'})
    Pages = []
    print(res)
    for i in res:
        print(i.text)
