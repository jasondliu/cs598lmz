import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Fizz'*(i%3<1)+'Buzz'*(i%5<1) or str(i) for i in range(1,101)))).start()

## FizzBuzz in C
#include<stdio.h>
#define p(n)for(int i=1;i<n+1;i++)printf(i%15?i%3?i%5?"%d\n":"Buzz\n":"Fizz\n":"FizzBuzz\n",i);
#define P(n)for(int i=1;i<n+1;i++)printf(i%3?i%5?"%d ":"Buzz ":"Fizz ",i);
#define P1(n)printf("1 ");P(n)
#define P2(n)P1(n)p(n)
#define P3(n)P1(n);p(n)P1(n)
#define P4(n)P2(n)P2(n)
#define P5(n)P2(
