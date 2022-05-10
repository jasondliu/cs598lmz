import gc, weakref

class MyObject(object):
    def __init__(self):
        print "Object created."

    def __del__(self):
        print "Object deleted."

def main():
    obj = MyObject()
    obj_id = id(obj)
    print "Object id:", obj_id

    # Manually delete the object
    del obj

    # Check if object is available
    print "Object available:", gc.get_referents(obj_id)

if __name__ == "__main__":
    main()
