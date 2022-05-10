import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])</code>

and it works as expected under WinXP and Windows Server 2003 x86 (<code>v6.1.7601</code>),
but I saw the strange results under <code>Windows 95</code> (<code>v4.0</code>, but it's not matter), what can do such things,
if someone can explain why this code doesn't works under <code>Windows95</code>, <code>MS Visual C++ 6.0</code> and <code>Python 2.0</code>,
please comment or answer below.


A:

Believe it or not, your code works on my Windows 95 machine. But in order to get it to work, I had to make a few tweaks:

Raise the stack limit. The default for Windows 3.1 is 10000 bytes - you'll need much more than that! In MSVC, altering <code>/STACK</code> in the Project menu (for each project) would do the job.
Make sure that you call <code>naked</code> from a DLL, not from your EXE. Stackspace is allocated from the bottom up, and an executable has to leave
