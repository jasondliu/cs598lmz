from bz2 import BZ2Decompressor
BZ2Decompressor

with open('./data/amazon_meta.txt.bz2', 'rb') as f:
    in_file = BZ2File(f)
    for line in in_file:
        if (str(line).__contains__('ASIN')): # get the line having the ASIN
            reviews_asin.append(line[5:14]) # get the first line asin values
            count += 1
            if(count==n_o_r):
                break
reviews_asin[:5]

%%time
reviews = pd.DataFrame()
id=0
for asin in reviews_asin:
    reviews.loc[id,"asin"] = asin
    help_rating = []
    overall_rating = []
    review_date = []
    reviewer_name = []
    music_style = []
    review_text = []
    for line in in_file:
        if(line!='\n'):
            if(str(line).__contains__('helpful')):
                help_rating.append(str(line).split('
