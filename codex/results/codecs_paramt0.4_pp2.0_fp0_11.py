import codecs
codecs.register_error('ignore', codecs.lookup('utf-8')[2])

# 크롤링한 데이터를 저장할 디렉토리
save_dir = "./data/raw/"

# 크롤링할 단어 리스트
word_list = ['삼성전자', '엘지전자', '신한지주', '현대차', '아모레퍼시픽', '삼성바이오로직스', '현대모비스', '셀트리온', '한국전력', 'SK하이
