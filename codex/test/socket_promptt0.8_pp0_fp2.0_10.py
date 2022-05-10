import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # get the first interface
    for i in range(1, 100):
        try:
            name = socket.if_indextoname(i)
        except ValueError:
            continue
        break
    print(i, repr(name))
    assert name != ''

    try:
        socket.if_indextoname(0)
    except ValueError:
        pass
    else:
        raise TestFailed('ERROR: if_indextoname should fail with correct index')

if __name__ == "__main__":
    test_if_indextoname()
