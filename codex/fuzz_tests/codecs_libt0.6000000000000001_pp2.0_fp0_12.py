import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# set the urls
url = "https://www.kijiji.ca/b-appartement-condo/ville-de-montreal/c37l1700281"

# read the html file
with open("./html/kijiji_apartment_page.html", "r") as file:
    kijiji_apartment_page = file.read()

# use BeautifulSoup to parse the html
soup = BeautifulSoup(kijiji_apartment_page, "html.parser")

# find all the items in the list
kijiji_items = soup.find_all("div", class_="search-item")

# print the number of items returned
print(f"{len(kijiji_items)} items returned.")

# get the data from each item
for item in kijiji_items:

    # get the title, price, and link
    title = item.find("a", class_="title").text
