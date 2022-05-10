from lzma import LZMADecompressor
LZMADecompressor('easy_install lzma').decompress(x)
</code>
Вылетает ошибка:
<code>lzma.LZMAError: Input format not supported by decoder
</code>
Раньше я игрался с модулем lzma, и кажется всё работало. Информации не нашел, т.е. что может вызывать это исключение. Перестало работать не давно.
OS: win7-64bit, python-2.7.9 32bit
На питоне 3.4 т
