import bz2
bz2.decompress(bz2_data)

# 해당 단어를 찾아서, 개수를 리턴하는 함수
def get_count(word):
    return bz2_data.count(word.encode('utf-8'))

a_count = get_count('a')
print(a_count)

b_count = get_count('b')
print(b_count)

# 전체 단어의 개수를 구하는 함수
def get_total_words_count():
    return len(bz2_data.split())

total_words_count = get_total_words_count()
print(total_words_count)


# 빈도수 구하는 함수
def get_frequency(
