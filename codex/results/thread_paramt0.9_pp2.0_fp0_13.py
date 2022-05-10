import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
```

This works in a similar way to [the last one](#reference-python-pypy-ruby-jruby-tcl), but this time it is aware of the platform it is running on (the `:\n` part is obviously windows only).

##### Reference Javascript, Node.js
The last couple of solutions have been clever and minimal, but how about some really minimal:
```javascript
[1,0,0].map(readline)
```
This reads in three lines of input, which are inserted into the array. However, this does something interesting. When arrays are converted to strings, any non-string elements are instead converted to their string representation. This means that as an array, it is equivalent to inputting the three lines, but if it is converted to a string, it becomes `100`:
```javascript
JSON.stringify([1,0,0].map(readline));
```

A slightly trickier alternative is:
```javascript
let input = '';
readline.createInterface({ input: process.stdin, output: process
