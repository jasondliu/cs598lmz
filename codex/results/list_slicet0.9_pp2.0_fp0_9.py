import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
del lst
print("문제 63. 위의 코드의 출력 결과는 무엇인가?")
print("문제 64. 파이썬의 이용면에서 어떻게 보면 문자열은 숫자의 한종류일까?")
print("문제 65. (별점)다음은 '0' 문자를 출력하기 위해 코드가 정확하지 않습니다. 수정해 보시오.")
print("문제
