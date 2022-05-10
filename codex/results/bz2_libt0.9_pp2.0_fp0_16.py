import bz2
bz2.decompress()


def run():
    letters = collections.defaultdict(int)
    data = bz2.decompress(urlopen('http://www.pythonchallenge.com/pc/def/integrity.html.bz2').read())
    user = re.search(r'un: \'(.*)\'', data).group(1)
    pw = re.search(r'pw: \'(.*)\'', data).group(1)
    print(user, pw)
    # results = [ord(letter) for letter in re.findall('\d+', data)]
    # urllib.parse.quote_plus(datum)



if __name__ == '__main__':
    run()
