import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

df_covid19 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

df_covid19 = df_covid19.drop(['UID','iso2','iso3','code3','FIPS','Admin2','Country_Region','Lat','Long_','Combined_Key'], axis = 1).groupby('Province_State').sum()

df_covid19['date'] = df_covid19.columns
df_covid19 = df_covid19.melt(id_vars=['date'])
df_covid19 = df_covid19.rename(columns = {'Province_State':'state', 'date':'date', '
