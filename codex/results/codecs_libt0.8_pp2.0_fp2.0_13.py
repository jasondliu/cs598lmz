import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

def get_link(link):
    r = requests.get("https://www.tiktok.com/" + link)
    soup = BeautifulSoup(r.text , "html.parser")
    try:
        link = soup.find("script" , {"type":"application/ld+json"}).text
        link = json.loads(link)["contentUrl"]
    except:
        try:
            link = soup.find("script")
            link = link.text.split('videoUrl')[1].split(',')[0].replace('":"',"")
            link = link.replace('"',"")
            link = link.replace("\\","")
        except:
            pass
    return link

def run():
    try:
        username = sys.argv[1]
    except:
        pass
    url = "https://www.tiktok.com/@" + username
    r = requests.get(url)
    soup =
