import sys, threading

def run():
    threading.Thread(target=print, args=("fuck you.\n",)).start()
    time.sleep(2)
    sys.stdout.write("the end\n")
</code>
I want python to print <code>the end</code> and then <code>fuck u</code>

The actual code:
<code>import sys, threading
import neural

def run():
    threading.Thread(target=neural.get_neural_network, args=("test",)).start()
    time.sleep(2)
    sys.stdout.write("test")
</code>
<code>get_neural_network</code> is a function that get a <code>network.json</code> (e.g., a model) from a directory named <code>test</code>
and the write it to the current working directory.
when the function is finished, he print something like this:
<code>get_neural_network finished "1 hour ago"
</code>
With the real function and not the example code, it prints <code>the end</
