import threading
# Test threading daemon
threading.Thread(target=main).start()
</code>
However, it has no apparent effect. The original thread still enters a hanging state until the subprocess finishes. And the subprocess still hangs when the original thread closes.
How can I fix this?


A:

It does not hang. Just press Ctrl+C:
<code>c:\Users\Nikita\IdeaProjects\python-sandbox&gt;python .\temp.py
^CTraceback (most recent call last):
  File ".\temp.py", line 23, in &lt;module&gt;
    main()
  File ".\temp.py", line 17, in main
    subprocess.run(["my-sub-process", "--some-opt"])
  File "C:\Users\Nikita\AppData\Local\Programs\Python\Python37\lib\subprocess.py", line 472, in run
    with Popen(*popenargs, **kwargs) as process:
  File "C:\Users\Nikita\AppData\Local\Programs\Python\Python37\lib\subprocess.
