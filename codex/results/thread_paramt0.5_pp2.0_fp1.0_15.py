import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def check_prime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False
    else:
        print(n, "is a prime number")
        return True


for n in range(1, 20):
    check_prime(n)

#class PrimeNumber(threading.Thread):
#    def __init__(self, number):
#        threading.Thread.__init__(self)
#        self.Number = number
#
#    def run(self):
#        counter = 2
#        while counter*counter < self.Number:
#            if self.Number % counter == 0:
#                print("{} is no prime number, because {} = {} * {}".format(self.Number, self.Number, counter, self.Number / counter))
#                return
#           
