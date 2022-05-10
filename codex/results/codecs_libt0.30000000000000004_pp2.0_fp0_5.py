import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Set the working directory
os.chdir('C:/Users/james/Desktop/Python/Python_Projects/Python_Projects/Web_Scraping')

# Create the dataframe
df = pd.DataFrame()

# Get the data
for i in range(1, 6):
    # Get the data
    url = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015&start=' + str(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Get the table
    table = soup.find_all('table')[0]
    
    # Get the data from the table
    data = [[td.text for td in row.find_all('td')] for row in table.find_all('tr')]
    
    # Get the headers
    headers = [th.text for th
