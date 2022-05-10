import sys, threading

def run():
    for i in range(1000000):
        with open('data.txt', 'a') as f:
            f.write('%d\n' % i)
        with open('data.txt', 'r') as f:
            data = f.read()
        sys.stdout.write(data)

t1 = threading.Thread(target = run)
t1.start()
t2 = threading.Thread(target = run)
t2.start()
</code>
When I run this code with python I get the following error:
<code>unexpected end of file.
</code>
What is the reason for this error and how can I fix it?

