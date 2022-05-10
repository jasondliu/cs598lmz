import sys, threading

def run():
    while True:
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    main()
</code>
I get the following output:
<code>$ python test.py
..........
</code>
The <code>\n</code> is not printed.
If I change the <code>sys.stdout.write('\n')</code> to <code>sys.stdout.write('\n\n')</code> I get the following output:
<code>$ python test.py
..........


</code>
So the <code>\n</code> is not printed, but the <code>\n\n</code> is printed.
If I change the <code
