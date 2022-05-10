import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)


class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.soup = None
        self.soup = BeautifulSoup(open(filename), 'html.parser')

    def get_products(self):
        return self.soup.find_all('div', attrs={'class': 'product_container'})

    def get_name(self, product):
        return product.find('div', attrs={'class': 'product-item-info'}).find('a').text.strip()

    def get_image(self, product):
        return product.find('div', attrs={'class': 'product-image-photo'}).find('img')['src']

    def get_url(self, product):
        return product.find('div', attrs={'class': 'product-item-info'}).find('a')['href']

    def get_price(self, product):
        return product
