import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
# postgresql db connection
engine = create_engine('postgresql://postgres:postgres@localhost:5432/e_commerce')

# read data from sql db
df = pd.read_sql_query('select * from orders',con=engine)

# create new dataframe with only needed columns
df = df[['order_id','order_item_id','product_id','seller_id','customer_id','order_status','price','freight_value','payment_type','payment_installments','payment_value','review_score','review_comment_title','review_comment_message','review_creation_date','review_answer_timestamp']]

# change data type to datetime
df['review_creation_date'] = pd.to_datetime(df['review_creation_date'])
df['review_answer_timestamp'] = pd.to_datetime(df['review_answer_timestamp'])

# create new columns for
