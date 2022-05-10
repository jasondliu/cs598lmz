import signal
signal.signal(signal.SIGINT, handler)


url = 'https://www.dotabuff.com/heroes/counter-picks'
response = urlopen(url)
html = response.read()

parsed_url = urlparse(url)
end = parsed_url[2].split('/')[2]

pattern = re.compile('<div class="hero-grid-item"><a class="image-hero-grid-item" href="/heroes/[0-9][0-9][0-9][0-9][0-9]">')
counter = 0
for match in pattern.finditer(html):
    if counter == 5:
        break

    url = match.group(0)
    url = url[url.find('/heroes'):url.find(">")]
    url = parsed_url[0] + '://' + parsed_url[1] + url
    response = urlopen(url)
    html = response.read()
    
    pattern = re.compile('<div class="image-container "><
