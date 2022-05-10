import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\Users\deepak\Desktop\yoga\wallpaper.jpg" , 0)
#SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\Users\deepak\Desktop\yoga\wallpaper.jpg", SPIF_UPDATEINIFILE)

# get today's date
todays_date = date.today()

# convert to format to be used in url
todays_date_str = todays_date.strftime("%m-%d-%Y")

# create the url
url = "https://www.brainyquote.com/quote_of_the_day"

# make the request
response = requests.get(url)

# parse the response
soup = BeautifulSoup(response.content, "html.parser")

# find the quote
quote = soup.find("img", {"class": "p-qotd"})

# find the author
author = soup.find("a", {"title": "view quote author"})


