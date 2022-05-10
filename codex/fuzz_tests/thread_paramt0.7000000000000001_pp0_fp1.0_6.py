import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world")).start()


# In[ ]:


#6.2
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world")).run()


# In[ ]:


#6.3
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world")).start().join()


# In[ ]:


#7.1
def f():
    yield 1
    return
    yield 2
print(f())


# In[ ]:


#7.2
def f():
    yield 1
    yield 2
print(f())


# In[ ]:


#8.1
def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()
f()


# In[ ]:


#8.2
def f():
