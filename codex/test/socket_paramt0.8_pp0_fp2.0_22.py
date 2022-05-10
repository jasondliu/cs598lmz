import socket
socket.if_indextoname(socket.if_nametoindex(interface))


# In[ ]:


# Python program to convert decimal number into binary using recursion 
  
def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
      
# decimal value  
dec_val = 34
  
# Calling function 
DecimalToBinary(dec_val) 


# In[ ]:


# A recursive Python program to find LCA of two nodes n1 and n2 
  
# A Binary tree node 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
  
# Finds the path from root node to given root of the tree, Stores the 
# path in a list path[], returns true if path exists otherwise false 
