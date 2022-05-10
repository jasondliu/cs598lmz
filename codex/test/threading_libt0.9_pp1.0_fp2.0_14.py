import threading
threading.stack_size(65536)

sys.setrecursionlimit(2**20)

comments = pd.read_csv('./data/twitter_comments_1125.csv')
 
comments.comments = comments.comments.apply(lambda x:BeautifulSoup(x).get_text())

comments.comments = comments.comments.apply(lambda x:re.sub('[^a-zA-Z]',' ',x))

print(comments['main_tag'].unique())
print(comments['sub_tag_1'].unique())
print(comments['sub_tag_2'].unique())
comments = comments[comments['sub_tag_2'].isin([ 'Apparel','Beauty_Products_and_Accessories',
                 'Footwear',
                 'Others',
                 'Photo',
                 'Sports_and_Travel_Goods'])]

X = comments['comments'].values
y = comments['sub_tag_2'].values

