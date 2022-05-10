import sys, threading

def run():
    print "Hello"

def main():
    t = threading.Thread(target=run)
    t.start()
    t.join()

if __name__ == '__main__':
    main()
</code>
I am using the following command to run the code:
<code>python -m cProfile -s cumulative test.py
</code>
The output is:
<code>Hello
         4 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 &lt;string&gt;:1(&lt;module&gt;)
        1    0.000    0.000    0.000    0.000 test.py:10(main)
        1    0.000    0.000    0.000    0.000 threading.py:1056(__bootstrap)
        1    0.000    0.000    0.000    0.000 threading.
