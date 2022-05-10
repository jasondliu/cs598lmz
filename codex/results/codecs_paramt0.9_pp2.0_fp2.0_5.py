import codecs
codecs.register_error('strict', codecs.ignore_errors)
import catalog.colours

catalog.colours.credits()

url       =  "https://www.darklyrics.com" + sys.argv[1]
file_name =  sys.argv[1][1:-4] + 'txt'
soup      =  BeautifulSoup(requests.get(url).content, 'lxml')

# page_lines  =  soup.findAll("div", {"class":"lyrics"})
album_name =  soup.findAll("div", {"class":"album"})[0].text
year_url   =  soup.findAll("div", {"class":"album"})[0].findAll('a')[0]['href']
year       =  BeautifulSoup(requests.get(url + year_url).content, 'lxml').findAll("div", {"id":"content-r"})[0].findAll("div", {"class":"sen"})[1].text
artist     =  soup.findAll("div", {"class":"album"})[0].findAll('a')[
