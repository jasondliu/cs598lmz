from types import FunctionType
a = (x for x in [1])
a.__name__
(*[1],) # (*)은 하나의 요소만 쓸 수 있고 리스트를 하나만 쓸 수 있다.
time.sleep(0.05)
# time.sleep은 시간을 줘서 지연시킬 때 쓰며 프로그램을 강제 종료시킨다.
print("Umut")
time.sleep(0.05)
print("Civan")
time.sleep(0.05)
print("EKOK")

def my_sum(*numbers):
    print(numbers)
    if len(numbers) == 0:
        return 0
    else:
        sum = 0
        for number in numbers:
            sum =
