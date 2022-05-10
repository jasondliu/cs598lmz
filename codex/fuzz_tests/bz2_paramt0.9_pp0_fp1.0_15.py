from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(base64.b64decode("".join(parsed_body.split("\n")[1:])))

def get_url(day, data):
  url = "http://adventofcode.com/day/{}/input".format(day)
  response = requests.get(url, cookies={"cookie": data})
  html = response.text
  opener = re.search("<article class=.day-desc", html)
  ender = re.search("</article>", html[opener.end():])
  body = html[opener.end():][ender.end():].strip()
  return body
