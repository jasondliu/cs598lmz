import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def wait_for_enter():
    raw_input("Press enter to continue.")

def print_dict_keys(d):
    print "Keys:"
    print d.keys()
    print

def print_dict_values(d):
    print "Values:"
    print d.values()
    print

def print_dict_items(d):
    print "Items:"
    print d.items()
    print

def print_dict_items_by_key(d):
    print "Items by key:"
    for k in sorted(d.keys()):
        print k, ":", d[k]
    print

def print_dict_items_by_value(d):
    print "Items by value:"
    for k, v in sorted(d.items(), key=lambda x: x[1]):
        print k, ":", v
    print

def print_dict_items_by_length(d):
    print "Items by length:"
    for k, v in sorted(d
