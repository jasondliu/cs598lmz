import sys, threading

def run():
    print(sys.argv[1])
    g = agate.Table.from_csv(sys.argv[1], encoding='utf-8')
    g.to_csv('output.csv', encoding='utf-8')

def main():
    t1 = threading.Thread(target=run)
    t1.start()
    t1.join()

if __name__ == '__main__':
    main()
</code>
When I run it using <code>python3 test.py test.csv</code>, it goes into an infinite loop printing <code>test.csv</code> over and over.  If I make it not a thread, it runs as expected.  It seems to be a problem with the <code>agate</code> library.
How do I make this work as a thread?


A:

The problem was that I was using a virtualenv.  Once I installed the <code>agate</code> library in the global environment, it worked correctly.

