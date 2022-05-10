import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class Process:
    def __init__(self):
        pass

    def fetch_data(self):
        data = []
        for index in range(1, 65):
            page = 'https://www.newegg.com/global/tw-zh/p/pl?d=gpu&page=' + str(index)
            htmlfile = urllib.urlopen(page)
            htmltext = htmlfile.read()
            regex = '<div class="item-info.*?</li>'
            pattern = re.compile(regex)
            item_info_array = re.findall(pattern, htmltext)
            regex = 'href="(.*?)"'
            pattern = re.compile(regex)
            for item_info in item_info_array:
                item_info = item_info.replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
                url
