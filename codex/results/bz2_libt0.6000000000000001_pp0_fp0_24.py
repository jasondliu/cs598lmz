import bz2
bz2_file = bz2.BZ2File('train.ft.txt.bz2')
for line in bz2_file:
    print(line)
    break

# 4.12.3.3. 임베딩을 사용하여 문장 데이터를 벡터 표현하기
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

# 단어 수를 제한하고 빈도 수가 높은 단어만 선택
max_words = 1000

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(train_texts)
sequences = tokenizer.texts_to_sequences(train_texts)

word_index = tokenizer.word_
