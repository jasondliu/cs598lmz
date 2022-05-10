import types
types.FunctionType

# from http://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
import sys

try:

    # Create a function whose globals would have an 'undefined'
    if 1:
        def sample(x):
            "This is the docstring of a function that accesses undefined"
            return 9

    # Get at the globals
    gbl = sample.__globals__

    # Poke a value into test.x
    if 0:
        gbl["x"] = 23

    # And if we use the magic of sys._getframe...
    assert gbl == sys._getframe(1).f_globals
    if 0:
        print "Hooray!"

except:
    print >> sys.stderr, "You don't have sys._getframe"

import MetaStyle


# tpl = ("""<tr><td class="%s">%s</td><td>%s</td><td>%s</td></tr>\n""" %
# )

area = cgi
