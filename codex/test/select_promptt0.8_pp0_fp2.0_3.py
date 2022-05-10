import select
# Test select.select
def select01():
    real = select.select
    def mock(r, w, x, timeout):
        return [], [1], []
    select.select = mock
    f = open('./select.py')
    try:
        f.write('hello')
    except IOError:
        print('caught IOError')
    finally:
        select.select = real
        f.close()
# Test file.truncate
def truncate01():
    f = open('./truncate.py', 'w')
    f.write('hello world')
    f.truncate(5)
    f.close()
    assert os.stat('./truncate.py').st_size == 5
# Test file.write
def write01():
    f = open('./write01.py', 'w')
    f.write('hello world')
    f.write('hello world2')
    f.close()
    assert os.stat('./write01.py').st_size == 21
# Test file.write
