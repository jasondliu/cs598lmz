import bz2
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

import bs4
def parseData(get_data, number=1):
    data = []
    soup = bs4.BeautifulSoup(get_data, "html.parser")
    for i in range(number):
        tag = soup.find_all("tr")[i+1]
        line = []
        for el in tag:
            line.append(str(el)[4:-4].replace(", "," - "))
        line.remove('')
        data.append(line)
    return data
file = open("C:/Users/Michael/Downloads/7824-h.htm","r", encoding="UTF-8")
data = parseData(bz2.decompress(
