import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(str())
del keepali0e,lst,a
gc.collect()


# In[13]:


from weakref import WeakKeyDictionary
class Grade(object):
    def __init__(self):
        self._values=WeakKeyDictionary()
    def __get__(self,instance,owner):
        if instance is None:
            return self
        return self._values.get(instance,0)
    def __set__(self,instance,value):
        if not (0<=value<=100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance]=value
class Exam(object):
    math_grade=Grade()
    writing_grade=Grade()
    science_grade=Grade()
first_exam=Exam()
first_exam.writing_grade=82
second_exam=Exam()
second_exam.writing_grade=75
second_exam.math_grade=80
first_exam.writing_grade


# In[14]:


