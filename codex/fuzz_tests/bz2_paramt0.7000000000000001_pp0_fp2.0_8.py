from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(solution)

#solution = solution.decode('utf-8')

solution

with open('solution.txt', 'w') as fhand:
    fhand.write(solution)

#html = solution
#
#from bs4 import BeautifulSoup
#import re
#
#soup = BeautifulSoup(html, 'html.parser')
#
#tags = soup('a')
#
#for tag in tags:
#    print(tag.get('href', None))
#
#print(tags)
