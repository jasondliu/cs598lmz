import types
types.NoneType
# <class 'NoneType'>

def list_sum(list_val):
    if len(list_val) == 1 :
        return list_val[0]
    else :
        return list_val[0] + list_sum(list_val[1:])

list_sum([1,2,3])
# 6

# def list_sum(list_val):
#     if list_val == [] :
#         return 0
#     else :
#         return list_val[0] + list_sum(list_val[1:])



def toStr(n, base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))
# 5AD

def game(num):
    print("I'm thinking of a number between 1 and 100. Try to guess my number.")
