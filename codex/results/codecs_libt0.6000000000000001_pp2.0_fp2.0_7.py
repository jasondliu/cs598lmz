import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Set the working directory
os.chdir("C:/Users/Yi/Dropbox/Harvard/2016-2017/THA/Data/")

# Import the data
data = pd.read_csv("tha_data.csv", sep = ",")

# Create a list of unique clusters
cluster_list = pd.Series.unique(data['cluster'])

# Create a list of unique years
year_list = pd.Series.unique(data['year'])

# Create a list of unique years
country_list = pd.Series.unique(data['country'])

# We will use all the variables in the regression
var_list = ['gdp_pc_pp', 'gdp_growth', 'gdp_pc_growth', 'gdp_pc_pp_growth', 'gdp_pc_pp_growth_sq',
            'gdp_pc_pp_growth_cu', 'gdp_pc_growth_sq',
