import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

print('foo')

# Output:
# .foo
</code>
<blockquote>
<p><strong>Question 2:</strong> Now each time the program is run, <code>&lt;code&gt;.foo&lt;/code&gt;</code> is printed on a new line, with the period on the previous line. How can I make it so that <code>&lt;code&gt;.foo&lt;/code&gt;</code> is printed on the same line each time the program is run?</p>
</blockquote>

