import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='yelp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



#print(yelp_business_data['business_id'])
#print(yelp_tip_data['business_id'])

#yelp_business_data['business_id'].isin(yelp_tip_data['business_id']==True)

a=yelp_business_data.business_id.isin(yelp_tip_data.business_id)

b=yelp_business_data.loc[a,]

#print(b)

#yelp_business_data[yelp_business_data.business_id==yelp_tip_data.business
