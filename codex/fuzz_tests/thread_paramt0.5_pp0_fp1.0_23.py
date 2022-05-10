import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# ###############################################

# Reading input from STDIN
import sys

def main():

    # Write code here 
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    s = 0
    for i in range(1, n):
        if a[i] == a[i-1] + 1: s += c[a[i-1]-1]
    print(s+b[a[0]-1]+b[a[n-1]-1])

main()

# ###############################################

# Python 3 program to find maximum  
# sum such that no two elements 
# are adjacent 
  
# Function to return max sum such that  
# no two elements are adjacent 
def find_max_sum(arr): 
      
    incl = 0
    excl = 0
      
    for i in arr: 
