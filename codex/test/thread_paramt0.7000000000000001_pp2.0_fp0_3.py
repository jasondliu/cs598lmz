import sys, threading
threading.Thread(target=lambda:sys.stdin.readline()).start()

#------------------------------------------------------------------------------
# This function takes in a number n, and returns all the primes that are less
# than n.

def find_primes_below_n(n):
    
    # We first create a list of all the integers from 2 to n - 1.
    numbers = range(2,n)
    # Then we create an empty list to store the primes we find.
    primes = []
    
    # This while loop continues until all the numbers in the list are gone.
    while len(numbers) > 0:
        
        # The first number in the list is a prime.
        # We add it to the primes list.
        p = numbers.pop(0)
        primes.append(p)
        
        # Then we remove all multiples of this prime from the list.
        # We do this by creating a new list which is a copy of the
        # original numbers list.
        new_numbers = list(numbers)
        
        # Then we loop through all the numbers in new_numbers
