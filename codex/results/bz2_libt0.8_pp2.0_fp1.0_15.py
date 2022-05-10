import bz2
bz2.decompress(page)
 
# Now let's try for the next link. Traveling up and right at the same time.
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
import re
pat1 = r"and the next busynothing is (\d+)"
pat2 = r"Divide by two and keep going."

def busynothings(busy):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    resp = client.request(url+busy)
    page = resp.data
    print page, len(page)
    match = re.search(pat1, page)
    if match:
        next_busy = match.group(1)
        print next_busy
        busynothings(next_busy)
    else:
        print page
        return page
 
busynothings("12345")
resp = client.request("http://www.pythonchallenge.com/pc/def/linkedlist
