import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Make sure the paths are correct
path_to_data = "C:/Users/micha/OneDrive/Documents/GitHub/Data-Science-Projects/Python/Data/"
path_to_figs = "C:/Users/micha/OneDrive/Documents/GitHub/Data-Science-Projects/Python/Figures/"

# Read in the data
df = pd.read_csv(path_to_data + "covid_19_data.csv")

# Convert the dates to datetime objects
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
df['Last Update'] = pd.to_datetime(df['Last Update'])

# Get the number of cases per country
df_country = df.groupby(['Country/Region']).agg({'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum'})

# Get the number of
