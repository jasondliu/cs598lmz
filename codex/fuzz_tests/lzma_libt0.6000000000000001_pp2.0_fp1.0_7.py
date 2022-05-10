import lzma
lzma.decompress(b'\x00')

import threading

def test_thread_state():
    assert threading.get_ident() == threading.current_thread().ident

def test_thread_start():
    threading.Thread(target=test_thread_state).start()

def test_thread_join():
    t = threading.Thread(target=test_thread_state)
    t.start()
    t.join()

def test_thread_join_timeout():
    t = threading.Thread(target=test_thread_state)
    t.start()
    # we're in a single-threaded environment, so this should raise a
    # RuntimeError
    with pytest.raises(RuntimeError):
        t.join(timeout=0.001)
    t.join()

def test_thread_ident():
    assert threading.current_thread().ident == threading.get_ident()

def test_thread_daemon():
    t = threading.Thread(target=test_thread_state)
    assert not
