import bz2
bz2file = bz2.BZ2File('train.ft.txt.bz2', 'rb')
content = bz2file.readline()

print('BZ2 compressed file reads : \n {}'.format(str(content)))

# 압축에 사용된 모든 리뷰 수 
no_of_reviews = int(content.split(' ')[0])
print('Number of reviews : {}'.format(no_of_reviews))

no_of_unique_words = int(content.split(' ')[1])
print('Number of unique words in the dataset : {}'.format(no_of_unique_words))


# PPMI 행렬의 사이즈 : (Number of unique words)*(Number of unique words)

no_of_features = no_of_unique_words
PPMI_matrix = np.zeros((no_of_features , no_of_features))

from tqdm import tq
