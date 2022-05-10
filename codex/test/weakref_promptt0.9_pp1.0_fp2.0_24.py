import weakref
# Test weakref.ref function call with a finalizer

def func(a):
    print("Func called.", a)

def finalizer(obj):
    print("Finalizer called.", obj)

def main():
    try:
        ob = weakref.ref(object(), func, finalizer)
    except TypeError as e:
        print("Exception seen as expected: ", e)
    else:
        print("Call to weakref.ref succeeded but was not expected to")

if __name__ == "__main__":
    main()
