import weakref
# Test weakref.ref().

# Create a subclass of the class we're creating weak references to.
# It's ok if the subclass is in a different module.
import sub2

SubclassUser = sub2.SubclassUser

def main(args=None):
    import sys
    if args is None:
        args = sys.argv
    SubclassUser.add_to_module_dict(args)

    subuser = SubclassUser()
    del args
    with weakref.detect_cycles():
        wr = weakref.ref(subuser)
        del subuser
        if isinstance(wr(), SubclassUser):
            print ('weakref to subclass of User created successfully')
            print(wr())
        else:
            print('weakref to subclass of User failed')

if __name__ == '__main__':
    main()
