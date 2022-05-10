import threading
# Test threading daemon
def f(name):
    print('thread function', name)
    time.sleep(4)
    print('thread function', name, 'end')

if __name__ == '__main__':
    t = threading.Thread(target=f, args=('bob',), daemon=True)
    t.start()
    t.join()
    print('end')
</code>
Output:
<code>thread function bob
end
</code>
As you can see, no <code>thread function ... end</code> was printed, because the daemonic thread died immediately at the end of the main thread.

