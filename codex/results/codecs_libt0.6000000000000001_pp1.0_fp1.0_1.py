import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Load data from database
#engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/stock_crawler')
engine = create_engine('mysql+pymysql://stock:stock@localhost:3306/stock_crawler')

#engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/stock_crawler')

print "Load data from table"
df = pd.read_sql_table('twse_daily_price', con=engine)
df_date = pd.read_sql_table('twse_daily_price_date', con=engine)

df['date'] = pd.to_datetime(df['date'])
df_date['date'] = pd.to_datetime(df_date['date'])

df = df.sort_values(['code', 'date']).reset_index(drop=True)
df_
