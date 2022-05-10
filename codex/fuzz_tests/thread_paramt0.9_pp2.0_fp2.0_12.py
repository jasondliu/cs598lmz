import sys, threading
threading.Thread(target=lambda:sys.stdout.write("hello world")).start()

# will output "hello world" in python-mode
</code>
the only thing you really need to look at from pyevaluate is:
<code>def IsCommandLine(input_cmdline):
    if input_cmdline == "":
        return True
    return input_cmdline[0] == "!"
</code>
and:
<code>def FilterInputString(cmdline):
    if cmdline[0] == "!":
        return cmdline[1:]
    else:
        return cmdline
</code>
and that function is useful for any sort of multi-line interact mode in emacs
you can find it here:
<code>(defun python-shell-send-string (string &amp;optional process add-to-history)
  "Send the STRING to inferior Python PROCESS.
When optional argument ADD-TO-HISTORY is non-nil, add STRING to
the history.  This is only called when SENDING a string."
  (python-shell-send-string-no-output string process))

