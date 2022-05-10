import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Set the working directory
os.chdir(r'C:\Users\james\Documents\GitHub\mapping-project')

# Import the data
data = pd.read_csv('data/data.csv')

# Create a list of the unique locations
locations = data['location'].unique()

# Create a list of the unique years
years = data['year'].unique()

# Create a list of the unique years
years = data['year'].unique()

# Create a list of the unique years
years = data['year'].unique()

# Create a list of the unique years
years = data['year'].unique()

# Create a list of the unique years
years = data['year'].unique()

# Create a list of the unique years
years = data['year'].unique()

# Create a list of the unique years
years = data['year'].unique()

# Create a list of the unique years
years
