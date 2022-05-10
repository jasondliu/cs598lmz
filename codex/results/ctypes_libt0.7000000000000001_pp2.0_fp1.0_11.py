import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
</code>
This creates a Registry entry in HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppModel\Repository\Packages. 
I have lots of users and if I want them all to run this code, do I need to create a registry entry on all the user computers, or can I create it once on the server and the registry will be copied down to the user computers?

