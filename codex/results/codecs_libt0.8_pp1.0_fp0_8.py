import codecs
codecs.open('./sample_korean_10.txt', mode='r', encoding='utf-8').read()

# TF-IDF 값이 높은 단어순으로 정렬
import operator

tfidf_dict = dict()

for terms in terms_li:
    tfidf_dict[terms] = (1 + np.log10(terms_li.count(terms))) * np.log10(10 / (1 + word_count[terms]))

print(tfidf_dict)
sorted_dict = sorted(tfidf_dict.items(), reverse=True, key=operator.itemgetter(1))
print(sorted_dict)

# 파일 저장
with codecs.open('./sample_korean_10_tfidf.txt', mode='w', encoding='utf-8') as fp:
    for terms, tfidf in sorted_dict:
        fp.write("{0}\t{
