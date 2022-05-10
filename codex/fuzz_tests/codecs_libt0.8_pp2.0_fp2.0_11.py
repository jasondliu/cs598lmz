import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

def get_html(url):
    req = urllib.request.urlopen(url)
    html = req.read()
    return html

def get_result(html):
    tree = html.fromstring(html)
    title = tree.xpath("/html/head/title/text()")
    encoding = tree.xpath("/html/head/meta[@charset]/@charset")
    if not encoding:
        encoding = tree.xpath("/html/head/meta[@http-equiv='Content-Type']/@content")
    author = tree.xpath("//*[@name='author']/@content")
    keywords = tree.xpath("//*[@name='keywords']/@content")
    description = tree.xpath("//*[@name='description']/@content")
    return {
        "title": title,
        "encoding": encoding,
        "author": author
