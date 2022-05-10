import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
</code>
and the link below has more details
http://www.granneman.com/webdev/coding/what-happened-to-favicon-ico/
Misc.
Also check that you have a folder Favorites in C:\Users\username\Links and C:\Users\username\Favorites and that you have a current icon for a shortcut in there that is correct.
After changing it in the code above, try opening the folder above in Windows Explorer and see if the icon is correct. Then try using a program like this Program
The Process
If one or more of the above suggestions is valid then the next step is write the code that will install the shortcut.  An actual answer to this has been provided by Zack.
https://stackoverflow.com/a/49097475/813560

