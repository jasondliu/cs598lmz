import codecs
codecs.register_error('strict', codecs.ignore_errors)

def load_data():
	"""Load data into lists"""
	linkedin_companies = []
	linkedin_cities = []
	linkedin_dates = []
	f = codecs.open('linkedin.txt', 'r', 'utf-8', errors='ignore')
	for line in f:
		data = line.strip().split('\t')
		if len(data) == 3:
			linkedin_companies.append(data[0])
			linkedin_cities.append(data[1])
			linkedin_dates.append(data[2])
	return linkedin_companies, linkedin_cities, linkedin_dates

if __name__ == '__main__':
	linkedin_companies, linkedin_cities, linkedin_dates = load_data()
	print(str(len(linkedin_companies)) + ' companies')
	companies_unique_set = set(linkedin_companies)
	companies_unique = list(compan
