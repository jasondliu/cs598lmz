import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
</code>
but when I add the below line of code, I am getting some error saying as below:
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()

sys.stderr.flush()
NameError: name 'sys' is not defined
</code>
Can anyone please help me what went wrong here?


A:

Your code in the lambda isn't being executed, lambdas hold off on actually executing their body until they're called. Thus, they're unlikely to be useful for a thread target function, but that's not to say that the only problem you have here is using a lambda when it's not appropriate.
If you actually took a look at the line that the error is on, you might have figured this out, since <code>sys</code> isn't defined unless you're in the main scope:
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
print(sys)
