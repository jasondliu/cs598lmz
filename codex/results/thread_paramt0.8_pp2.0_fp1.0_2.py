import sys, threading
threading.Thread(target=lambda: open('C:\\Users\\MY NAME\\Documents\\folder\\'+arg, 'w')).start()
</code>
This works fine and a new folder named after the argument is created. The problem is that if the argument is 'New Folder', Windows will not allow that folder to be created.
So how can I create folders with arguments that are named like windows system folders and files?
Any help is greatly appreciated!
P.S. I don't want to create a new folder with a name like 'New Folder (1)' or 'New Folder - Copy' or something like that. I want to create a new folder with the name 'New Folder'.


A:

Instead of creating a folder why not just save the file with the name 'New Folder' if the folder can't be created.
<code>import os

if not os.path.isdir('C:\\Users\\MY NAME\\Documents\\folder\\New Folder'):
    threading.Thread(
        target=lambda: open('C:\\Users\\MY NAME\\Documents\\folder\\New Folder', 'w')
    ).start()
</code>

