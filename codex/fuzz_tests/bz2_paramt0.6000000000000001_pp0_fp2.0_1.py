from bz2 import BZ2Decompressor
BZ2Decompressor().decompress

# 함수에 추가적인 인자를 넘기고 싶다면 파라미터를 지정해 줘야 한다.

# 예를 들어 다음과 같이 함수를 정의할 수 있다.
def spam(a, b=42):
    print(a, b)

# 이때 spam 함수는 두 개의 파라미터를 가진다.
# 첫 번째 파라미터는 반드시 지
