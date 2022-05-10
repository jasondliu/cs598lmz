import threading
# Test threading daemon mode with timeout on join()

def sleeper(n):
    print('starting sleeper')
    time.sleep(n)
    print('end of sleeper')

t = threading.Thread(target=sleeper, name='daemon thread',
                     args=(4,))
t.daemon = True
t.start()

time.sleep(3)

print('main starting join')
print('daemon: {}'.format(t.daemon))
t.join(2)
print('main ending join')

print('is alive: {}'.format(t.is_alive()))
</code>
Result:
<code>starting sleeper
main starting join
daemon: True
end of sleeper
main ending join
is alive: False
</code>
Note that while <code>t.is_alive()</code> returns <code>True</code>, the output of the thread is ended.

