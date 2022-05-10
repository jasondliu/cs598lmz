import lzma
lzma.FILE_JS_HELP_URL
</code>
This has worked fine for me in the past. But now I'm getting the message "invalid syntax". What is wrong with the message?
By the way, it works fine if I type the following message into the interpreter but it does not work inside my script.
<code>import lzma
lzma.FILE_JS_HELP_URL
</code>


A:

Probably this is due to some extra space: http://bpaste.net/show/563649/
Let me know how it works out


