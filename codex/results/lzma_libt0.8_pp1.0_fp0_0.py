import lzma
lzma.check_is_supported()

# lzma.MODE_OPTIMAL
# lzma.FORMAT_AUTO/FORMAT_XZ/FORMAT_ALONE
with lzma.open('/home/pwc/Desktop/test_lzma.txt.xz', 'wt', encoding='utf-8') as f:
    f.write('Hello world!')

with open('/home/pwc/Desktop/test_lzma.txt', 'wt', encoding='utf-8') as f:
    f.write('Hello world!')

with open('/home/pwc/Desktop/test_lzma.txt', 'rb') as f_in:
    with lzma.open('/home/pwc/Desktop/test_lzma.txt.xz', 'wt', encoding='utf-8') as f_out:
        shutil.copyfileobj(f_in, f_out)

with lzma.open('/home/pwc/Desktop/test_lzma.txt.x
