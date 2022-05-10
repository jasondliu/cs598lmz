import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import os
os.system('C:\Python27\python.exe C:\Python27\Scripts\pyinstaller.exe --onefile --windowed --icon=C:\Users\x\Desktop\test.ico C:\Users\x\Desktop\test.py')
</code>
I get the error message:
<code>Traceback (most recent call last):
  File "C:\Python27\Scripts\pyinstaller-script.py", line 9, in &lt;module&gt;
    load_entry_point('PyInstaller==2.1', 'console_scripts', 'pyinstaller')()
  File "C:\Python27\lib\site-packages\PyInstaller\__main__.py", line 90, in run
    run_build(pyi_config, spec_file, **vars(args))
  File "C:\Python27\lib\site-packages\PyInstaller\__main__.py", line 46, in run_build
    PyInstaller.
