from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b) == False
print(type(a) == type(b)) == True
## ---------------


## -----------------
import datetime
C = datetime.datetime(2015,1,1,10,10)
print(C.second == 10) == True
## ---------------

## ----------------
# list comprehension
# Задание 4
# Дан список с записями температур в градусах по Фаренгейту и список с датами (такой же длины). Напишите цикл который будет переводить температу
