import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# get the table
url = "https://www.worldometers.info/coronavirus/"

# open a connection
uClient = uReq(url)

# read the page
page_html = uClient.read()

# close the connection
uClient.close()

# parse html
page_soup = soup(page_html, "html.parser")

# get the table
table = page_soup.findAll("table", {"class": "table table-bordered table-hover main_table_countries"})

# create a csv
filename = "covid19.csv"
f = open(filename, "w")
headers = "country, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, critical, total_cases_per_million, total_deaths_per_million\n"

# write the header
f.write(headers)

# loop
