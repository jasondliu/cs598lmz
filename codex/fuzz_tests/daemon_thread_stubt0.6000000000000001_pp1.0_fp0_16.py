import sys, threading

def run():
    sys.argv = ['', 'g:\\tmp\\main\\main.py']
    execfile('g:\\tmp\\main\\main.py')

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
</code>
Why can't I access the variables?

