import codecs
codecs.register_error('ignore_previously_decoded', partial(codecs.ignore_errors, errors='previously_decoded'))
def get_url(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'error'

def get_all(url):
    from lxml import etree
    import time
    html = etree.HTML(get_url(url), parser=etree.HTMLParser(encoding='utf-8'))
    html = html.xpath('//div[starts-with(@id, "post_")]/div[@class="post_wrapper"]')
    for h in html:
        if h.xpath('div[@class="post_top"]/div/h3/a/@href'):
            title = h.xpath('div[@class="post_top"]/div/h3/a/text()')[0]
            title = title.encode('gb18030', errors='ignore_previously_decoded
