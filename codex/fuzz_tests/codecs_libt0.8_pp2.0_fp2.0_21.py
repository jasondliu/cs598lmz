import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def getProd():
    data = []
    url = 'http://www.ssastores.com/impression/c/k-cup-pods?f_category_id=62#ce'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    products = soup.find_all("div", class_="view_item")
    for product in products:
        item = product.find("h3")
        brand = product.find("p", class_="brand")
        if brand is not None:
            brand = brand.text.replace("Brand: ", "")
        else:
            brand = "N/A"
        price = product.find("p", class_="price")
        if price is not None:
            price = price.text
        else:
            price = "N/A"
        line = brand + "|" + "Keurig K-Cup"
