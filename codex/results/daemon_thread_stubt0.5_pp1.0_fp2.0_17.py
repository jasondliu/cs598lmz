import sys, threading

def run():
    while True:
        sys.stdout.flush()
        sys.stderr.flush()
        time.sleep(1)

threading.Thread(target=run).start()

def get_response(url, headers=None):
    if headers is None:
        headers = {}
    try:
        response = requests.get(url, headers=headers)
        return response.text
    except:
        return ""

def get_soup(url, headers=None):
    html = get_response(url, headers)
    return BeautifulSoup(html, 'html.parser')

def get_json(url, headers=None):
    response = get_response(url, headers)
    return json.loads(response)

def get_tweets(url):
    soup = get_soup(url)
    tweets = []
    for li in soup.find_all("li", class_='js-stream-item'):
        if 'data-item-id' not in li.attrs:
            continue
        tweet = {
            'tweet
