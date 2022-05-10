import lzma
lzma_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file_lzma.py')
lzma.compile(lzma_path, target_dir=os.path.dirname(os.path.abspath(__file__)), optimize=2)
lzma.delete_source_upon_compilation = True
del lzma
</code>
My first question is: Does this cause any harm? Is it a problem that I compile and delete the file every time the program is run?
Second question:
There is another file named <code>lzma.py</code> located here on Windows 10:
<code>C:\Users\user\AppData\Local\Programs\Python\Python37-32\lib\lzma.py
</code>
Will the main Python program try to import that file or the file in my program folder? Is there a way to make sure it only uses the file in my program folder?

