import socket
socket.if_indextoname(3)

import pdb; pdb.set_trace()

#import pdb
#pdb.run('foo()')

#import pdb
#pdb.runcall(foo)

#import pdb; pdb.run('foo()')
#import pdb; pdb.runcall(foo)

#import pdb
#def bar():
#    pdb.set_trace()
#    print "Hello"
#bar()

#import pdb
#class Foo(object):
#    def bar(self):
#        pdb.set_trace()
#        print "Hello"
#Foo().bar()

#import pdb
#def bar():
#    try:
#        pdb.set_trace()
#        print "Hello"
#    except:
#        pass
#bar()

#import pdb
#def bar():
#    try:
#        1/0
#    except:
#        pdb.post_mortem()
#bar()

#import pdb
#def bar():
#    try
