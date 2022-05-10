import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()
print('main')


# --------------------------
# 3. 요소를 통합하여 결과를 생성하는 경우에는 제너레이터를 사용하자.
# --------------------------
# 코드를 작성할 때 무한 반복을 피하도록 신경써야 한다.
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'Four score and seven years ago...'

