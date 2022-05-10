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

def get_digits(n):
    '''
    Returns a list of digits from n
    '''
    return [int(i) for i in str(n)]

def is_palindrome(n):
    '''
    Returns True if n is a palindrome, False otherwise
    '''
    digits = get_digits(n)
    if digits == digits[::-1]:
        return True
    else:
        return False

def get_palindrome(n):
    '''
    Returns the palindrome of n
    '''
    digits = get_digits(n)
    digits_r = digits[::-1]
    return int(''.join(map(str, digits + digits_r)))

def is_lychrel(n):
    '''
    Returns True if n is a Lychrel number, False otherwise
    '''
    palindrome = get_palindrome(n)
    for i in range(50):
        reverse = int(''.join(map(str, reversed(get_digits(
