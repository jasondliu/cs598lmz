import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Google Map Downloader")

def download_map():
    # Set the URL you want to webscrape from
    url = 'https://www.google.com/maps/@35.6901063,139.7028983,15z'

    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    # To download the whole data set, let's do a for loop through all a tags
    for i in range(0, len(soup.findAll('img'))): #'a' tags are for links
        one_a_tag = soup.findAll('img')[i]
        link = one_a_tag['src']
        download_url = 'https://www.google.com'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('t='):])

def main():
    download_map()


