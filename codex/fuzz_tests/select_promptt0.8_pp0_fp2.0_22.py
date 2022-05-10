import select
# Test select.select

def test_select():
    assert select.select([], [], [], 0) == ([], [], [])

# Test slow calls

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)

def test_slowprint():
    import thread
    thread.start_new_thread(slowprint, ('Hello world!',))
    thread.start_new_thread(time.sleep, (10,))
    time.sleep(3)
