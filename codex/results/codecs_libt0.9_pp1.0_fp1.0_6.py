import codecs
codecs.register(lambda n: n.lower() if 'UTF8_SIG' else None)

# Read file
df_raw = pd.read_csv('C:/Users/LENOVO IDEAPAD 320/Documents/GitHub/Predicting-Power-Outages-The-Effect-of-Global-Warming/data.csv', encoding='utf-8-sig')
df_raw.head()

# Set Index Date
df_raw.set_index(['Date'], inplace=True)
df_raw.head()
df_raw.info()
df = pd.DataFrame(df_raw, columns = ['Date of Outage', 'Affected', 'Parishes Affected', 'Attending Crews', 'Venue', 'Reason / Emergency'])
df.info()

# Clean Data 
df['Parishes Affected'] = df['Parishes Affected'].str.replace(',', '')

# Split dataframe
df_reason = pd.DataFrame(df_raw, columns = ['Reason / Emergency'])
df_venue = pd
