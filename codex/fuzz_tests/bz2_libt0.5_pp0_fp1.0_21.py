import bz2
bz2.BZ2File(path).read()

with open(path) as f:
    payload = f.read()

# Convert the payload to a DataFrame
df = pd.read_csv(StringIO(payload.decode('utf-8')))

# Print the head of the DataFrame
df.head()

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)

# Get the title of Guido's webpage: guido_title
guido_title =
