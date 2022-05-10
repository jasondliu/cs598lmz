import codecs
codecs.register_error('strict', codecs.ignore_errors)
codecs.register_error('surrogateescape', codecs.surrogateescape_error)

EXIT_STATUS_SPIEGEL = 1
EXIT_STATUS_SZ = 2
EXIT_STATUS_READABILITY = 3

# https://stackoverflow.com/a/21912744/298633
def convert_unknown_encoding(data, encoding='UTF-8'):
    if type(data) == bytes:
        return data.decode(encoding)
    return data.encode(encoding)

def spiegel_extract_content(html):
    # TODO: html.xpath(".//script")[1]
    if len(html.xpath(".//div[@class='article-section']")) == 0:
        print("spiegel_extract_content: There are no article sections. Exiting.")
        #sys.exit(EXIT_STATUS_SPIEGEL)
        return None

    article = html.xpath(".//div[@class
