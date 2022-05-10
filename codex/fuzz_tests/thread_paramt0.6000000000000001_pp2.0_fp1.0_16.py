import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('{} * {} = {}'.format(a, b, a * b) for a in range(1, 11) for b in range(1, 11)))).start()


# In[7]:


# Python3 program to print alphabet A pattern 
  
# Function to display alphabet pattern 
def display(ch): 
    if(ch == 'E' or ch == 'A' or ch == 'D' or ch == 'O' or ch == 'P' or ch == 'R' or ch == 'B'): 
        print(ch, end = " ") 
    else: 
        print(ch) 
          
def alphabet(): 
    alpha = 65
    for i in range(0, 7): 
        for j in range(0, 7): 
            ch = chr(alpha + j) 
              
            # Calling function 'display' to print 
            # the alphabet 
            display(ch) 
        print() 
          
    for i in range(0, 7): 
        for j in
