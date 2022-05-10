fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

(a), (b), (_), (c), (d) = fn()

# diff
# No diff

##################################################
# No diff
##################################################
# expr = 'fn()\n'
# expr = ast.parse(expr)
# expr = GroupExpression(expr.body[0].value.args[0])
# expr.evaluate_forward({'fn': fn})
# expr.evaluate_backwards({'fn': fn})
a.value[0] = -1234567
a.gradients = {'value': 1}
b.gradients = {'value': 1}
c.gradients = {'value': 1}
d.gradients = {'value': 1}

##################################################
# No diff
##################################################
# expr = 'fn()\n'
# expr = ast.parse(expr)
# expr = GroupExpression(expr.body[0].value.args[0])
# expr.evaluate_forward({'fn': fn})
# expr.evaluate_backwards({'fn': fn})
a
