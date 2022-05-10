import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Pull in the data from the .csv file
data = pd.read_csv('/home/matthew/Documents/GitHub/matthewlehner.net/content/data/data.csv', encoding='cp65001')

# Create a new dataframe with just the columns we need
data_small = data[['Name', 'Title', 'Company', 'Location', 'Time', 'Date', 'Link', 'Description']]

# Create a new dataframe with only the rows that have a link
data_link = data_small[data_small['Link'].notnull()]

# Create a new dataframe with only the rows that have a description
data_desc = data_small[data_small['Description'].notnull()]

# Create a new dataframe that has both a link and a description
data_link_desc = data_link[data_link['Description'].notnull()]

# Create a new dataframe that has neither a link nor a
