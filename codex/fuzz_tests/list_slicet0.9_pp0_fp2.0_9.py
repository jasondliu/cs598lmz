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
</code>
In Cygwin Python 2.5.1, 64-bit CPU, this causes an OS crash with the message: <code>cygwin1.dll: *** fatal error - dumb heap (pass 6), heap 0x7c3f0000, data 0x017d0f9c, Win32 error 0</code>.


A:

I'd just like to expand on my comment in a standalone answer: The code you've posted simply does not do what you think you are trying to do. Thus, instead of this question being a 'what is the proper way to remove a reference cycle' question, it is actually a 'why does this code fail' question. The reason this code fails is because you are appending to a list in the middle of an iteration over that list. If you replace <code>lst.append(keepali0e[:])</code> with <code>newlst.append(keepali0e[:])</code> then this becomes a valid 'how do I remove a reference cycle' question.
As it stands, the code will leave a reference cycle even with the changes above. Appending a subset of keepali
