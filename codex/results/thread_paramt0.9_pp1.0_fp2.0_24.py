import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read()), daemon=True).start()
</code>
And now you can use the python file with <code>bash</code> to pipe inputs to command-line programs:
<code>$ seq 10 | python pipe.py python -c "print(input())"
1
2
3
4
5
6
7
8
9
10
</code>
If you have a lot of scripts, make a directory somewhere, such as <code>~/bin</code>, and add that directory to your <code>PATH</code> with:
<code>PATH="$HOME/bin:$PATH"
export PATH
</code>
In that directory, add the above <code>pipe.py</code> script and make it executable with:
<code>chmod +x pipe.py
</code>
Now you can create other scripts in that directory and make them executable.
When a bash script is invoked, it's checked to see if it's executable.  If it is, the kernel (not bash) executes the script.  If it has a <code>#!</
