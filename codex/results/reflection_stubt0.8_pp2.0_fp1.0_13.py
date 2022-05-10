fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi  # boom!
</code>
To investigate:
<code>import dis
dis.dis(dis.dis)
</code>
You'll see that it uses <code>get_instructions(...)</code> - a function of the <code>dis</code> module. It in turn uses the <code>dis.Bytecode(...)</code> class to interpret the bytecode. Now, the bytecode interpreter will happily interpret the bytecode, but the bytecode itself is invalid. The bytecode interpreter uses a <code>stack</code> and <code>pending</code> attributes to keep track of stack operations. I've modified <code>dis.Bytecode.__init__</code> in order to import <code>pdb</code> and break into a pdb session (debugging console) once the bytecode interpreter hits an error.
Here's some of the output:
<code>(Pdb) ?
Documented commands (type help &lt;topic&gt;):
========================================
EOF    apropos  pdb  run  unt
alias  args     q    s    until
b      break   
