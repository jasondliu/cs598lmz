import gc, weakref

class First(object):
    def __init__(self):
        self.s = 'text'
        self.calc = lambda x: x * 3

class Second(object):
    def __init__(self):
        self.s = 'text2'
        self.calc = lambda x: x ** 2
</code>
After, create an instance of the first class, and make a copy of the second class
<code>f = First()
s = copy.copy(s)
</code>
And this is where I get the problem
<code>is f.s is s.s # True
is f.calc is s.calc # False
</code>
However, if i do 
<code>import copy
f = First()
s = copy.deepcopy(f)

is f.s is s.s # True
is f.calc is s.calc # True
</code>
I have already done some research on this, but none of the reasons given have helped me figure out why the copy is doing this. Any suggestions or help would be appreciated.

